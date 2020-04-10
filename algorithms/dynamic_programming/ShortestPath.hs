{-# LANGUAGE FlexibleContexts #-}

import qualified Data.Set as Set
import qualified Data.Map as M

newtype Vertex t = Vertex t
    deriving (Show, Eq, Ord)

data Edge t = Edge { from :: Vertex t
                   , to :: Vertex t
                   , weight :: Int
                   }
                   deriving Show

data Graph t = Graph { vertices :: [Vertex t]
                     , edges :: [Edge t]
                     }
                     deriving Show


incomingEdges :: (Eq t) => Graph t -> Vertex t -> [Edge t]
incomingEdges (Graph _ egs) v = filter ((v ==) . to) egs

createGraph :: [String] -> [(String, String, Int)]-> Graph String
createGraph verts eds = Graph gVertices gEdges
    where gVertices = map Vertex $ (Set.toList . Set.fromList) verts
          gEdges = map toEdge eds
          toEdge (a, b, w) = Edge (Vertex a) (Vertex b) w

sampleVertices :: [String]
sampleVertices = ["A", "B", "C", "D", "E", "F", "G", "H"]

sampleEdges :: [(String, String, Int)]
sampleEdges = [ ("A", "B", 4)
              , ("A", "C", 2)
              , ("B", "C", 5)
              , ("D", "B", 6)
              , ("A", "D", 10)
              , ("B", "D", 10)
              , ("C", "E", 3)
              , ("E", "D", 4)
              , ("D", "F", 11)
              , ("G", "H", 11) -- Add separated edge to check if it works when there is no path
              ]

iNFINITY :: Int
iNFINITY = 9999999

-- This won't work if the graph is cyclic[Infinite Loop]
shortestPathNaive :: (Eq a) => Graph a -> Vertex a -> Vertex a -> ([Vertex a], Int)
shortestPathNaive g' s' t' = _shortestPathNaive g' s' t' ([], 0)
    where _shortestPathNaive g s t (path, wt)
            | s == t = (s:path, wt)
            | otherwise = selectMin $ map (\(Edge f _ w)-> _shortestPathNaive g s f (t:path, wt + w)) targetIncomings
            where targetIncomings = incomingEdges g t
                  selectMin = foldl (\(minPath, minW) (vs, w) -> if minW <= w then (minPath, minW) else (vs, w)) ([], iNFINITY)

-- The idea behind cycle breaking is to keep track of steps. If steps is greater
-- than the number of vertices in graph, just ignore that path
shortestPathNaiveCycleBreak :: (Eq a) => Graph a -> Vertex a -> Vertex a -> ([Vertex a], Int)
shortestPathNaiveCycleBreak g' s' t' = _sP g' s' t' ([], 0) 0
    where _sP g s t (path, wt) steps
            | steps > length (vertices g) = (path, iNFINITY)
            | s == t = (s:path, wt)
            | otherwise = selectMin $ map (\(Edge f _ w)-> _sP g s f (t:path, wt + w) (steps+1)) targetIncomings
            where targetIncomings = incomingEdges g t
                  selectMin = foldl (\(minPath, minW) (vs, w) -> if minW <= w then (minPath, minW) else (vs, w)) ([], iNFINITY)

-- TODO: start from here, use writer or state monad
shortestPathCycleBreakWithMemoization :: (Eq a, Ord a) => Graph a -> Vertex a -> Vertex a -> ([Vertex a], Int)
shortestPathCycleBreakWithMemoization g' s' t' = fst $ _shortestPathMemoization g' s' t' ([], 0) (0, M.empty)
    where _shortestPathMemoization g s t (path, wt) (steps, memo)
            | steps > length (vertices g) = let new = M.insert (s, steps) ([], iNFINITY) memo
                                             in (([], iNFINITY), new)
            | s == t = let new =  M.insert (s, steps) (s:path, wt) memo
                        in ((s:path, wt), new)
            | otherwise = case M.lookup (s, steps) memo of
                            Nothing -> selectMin $ map (\(Edge f _ w)-> _shortestPathMemoization g s f (t:path, wt + w) (steps+1, memo)) targetIncomings
                            Just a -> (a, memo)
            where selectMin = foldl (\((minPath, minW), m) ((vs, w), m') -> if minW <= w then ((minPath, minW), m) else ((vs, w), m')) (([], iNFINITY), M.empty)
                  targetIncomings = incomingEdges g t

main :: IO ()
main = do
    let graph = createGraph sampleVertices sampleEdges
    -- print $ shortestPathNaive graph (Vertex "A") (Vertex "F") -- This results infinite loop
    print $ shortestPathNaiveCycleBreak graph (Vertex "A") (Vertex "F")
    print $ shortestPathCycleBreakWithMemoization graph (Vertex "A") (Vertex "F")
