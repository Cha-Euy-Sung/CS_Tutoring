import Data.Hashable
import System.Environment

hashHawkid :: String -> Int
hashHawkid hawkid = hash hawkid

main :: IO ()
main = do
  args <- getArgs
  case args of
    [] -> putStrLn "This program should be run with your hawkid."
    hawkid : _ -> 
     do
       putStrLn (show (hashHawkid hawkid))
       return ()
