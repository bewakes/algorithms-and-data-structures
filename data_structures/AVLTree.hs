import System.Random
import Control.Monad

data AVLTree a =
      Empty
    | AVLTree a Int (AVLTree a) (AVLTree a)
    deriving Show

-- Factor is height of right subtree - height of left subtree which must be in {-1, 0, 1}

hasLeftSubtree :: AVLTree a -> Bool
hasLeftSubtree Empty = False
hasLeftSubtree (AVLTree _ _ Empty _) = False
hasLeftSubtree _ = True

hasRightSubtree :: AVLTree a -> Bool
hasRightSubtree Empty = False
hasRightSubtree (AVLTree _ _ _ Empty) = False
hasRightSubtree _ = True

-- TODO: start with fixing node factors
rotateLeft :: AVLTree a -> AVLTree a
rotateLeft Empty = Empty
rotateLeft (AVLTree a f l r)
  | hasLeftSubtree r = rotateLeft (AVLTree a f l (rotateRight r))
  | otherwise = let (AVLTree n f' _ r') = r in AVLTree n f (AVLTree a f l Empty) r'

rotateRight :: AVLTree a -> AVLTree a
rotateRight Empty = Empty
rotateRight (AVLTree a f l r)
  | hasRightSubtree r = rotateRight (AVLTree a f (rotateLeft l) r)
  | otherwise = let (AVLTree n f' l' _) = l in AVLTree n f l' (AVLTree a f Empty r)

insertWithFactorInfo :: (Ord a) => a -> AVLTree a -> (AVLTree a, Int)
insertWithFactorInfo i Empty = (AVLTree i 0 Empty Empty, 1)
insertWithFactorInfo i (AVLTree n f l r)
  | i < n = let (inserted, df) = insertWithFactorInfo i l
            in (AVLTree n (f - abs df) inserted r, if abs f <= abs (f - abs df) then 0 else 1)
  | otherwise = let (inserted, df) = insertWithFactorInfo i r
                in (AVLTree n (f + abs df) l inserted, if abs f <= abs (f + abs df) then 0 else 1)

insert :: (Ord a) => a -> AVLTree a -> AVLTree a
insert i tree = fst $ insertWithFactorInfo i tree


main :: IO ()
main = do
    -- randomInts <- replicateM 5 (randomRIO(0, 50) :: IO Int)
    -- let randomInts = [31,16,1,35,2,6,7,21,6,10,12,24,43,2,8]
    let randomInts = [8,6, 7,6]
    print randomInts
    let tree = foldr insert Empty randomInts
    print tree
    print $ rotateLeft tree
