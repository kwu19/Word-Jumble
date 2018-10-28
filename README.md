# Word-Jumble

## Anagrams and Word Jumbles 

A [word jumble](https://en.wikipedia.org/wiki/Jumble) is a word game where a randomized series of characters must be rearranged to spell a particular (English) word. For example the jumble `"plaep"` can be decoded as `"apple"`.

 1. Write a function `jumble_decode` that takes a jumbled word as an input parameter. 
    * It will generate all the anagrams for that jumbled word using the `anagrams` function (see below).
    <br/><br/>
    
    * Use a "dictionary file" (a text file listing all known English words) to filter out the the anagrams that are valid English words.
    <br/><br/>
    
    * This function must return a list of of valid English words. Please do **not** print the results.
<br/><br/>
 2. Write a function `anagrams` that will generate all the anagrams for a given word (in our case, we'll be providing it jumbled words. This function:
    * **must** use recursion to solve for the anagrams!
    <br/><br/>
    * **must** return a Python list of all generated anagrams (regardless of whether they are valid English words).
