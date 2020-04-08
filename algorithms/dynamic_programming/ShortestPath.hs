import qualified Data.Set as Set

newtype Vertex t = Vertex t
    deriving (Show, Eq)

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
incomingEdges (Graph _ edges) v = filter ((v ==) . to) edges

createGraph :: [String] -> [(String, String, Int)]-> Graph String
createGraph verts eds = Graph gVertices gEdges
    where gVertices = map Vertex $ (Set.toList . Set.fromList) verts
          gEdges = map toEdge eds
          toEdge (a, b, w) = Edge (Vertex a) (Vertex b) w

sampleVertices :: [String]
sampleVertices = ["A", "B", "C", "D", "E", "F"]

sampleEdges :: [(String, String, Int)]
sampleEdges = [ ("A", "B", 4)
              , ("A", "C", 2)
              , ("B", "C", 5)
              , ("D", "B", 6)
              -- , ("B", "D", 10)
              , ("C", "E", 3)
              , ("E", "D", 4)
              , ("D", "F", 11)
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
shortestPathNaiveCycleBreak g' s' t' = _shortestPathNaiveCycleBreak g' s' t' ([], 0) 0
    where _shortestPathNaiveCycleBreak g s t (path, wt) steps
            | steps > length (vertices g) = (path, iNFINITY)
            | s == t = (s:path, wt)
            | otherwise = selectMin $ map (\(Edge f _ w)-> _shortestPathNaiveCycleBreak g s f (t:path, wt + w) (steps+1)) targetIncomings
            where targetIncomings = incomingEdges g t
                  selectMin = foldl (\(minPath, minW) (vs, w) -> if minW <= w then (minPath, minW) else (vs, w)) ([], iNFINITY)

main :: IO ()
main = do
    let graph = createGraph sampleVertices sampleEdges
    -- print $ shortestPathNaive graph (Vertex "A") (Vertex "F")
    print $ shortestPathNaiveCycleBreak graph (Vertex "A") (Vertex "F")
