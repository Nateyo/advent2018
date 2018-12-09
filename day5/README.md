# Day 5 - Alchemical Reaction

## Star 1

One of the first thoughts for solving this problem is to make some kind of
dictionary of the reacting units, and iteratively replace them in the strings.
This solution will work fine, except for that fact that it will be very slow.
With a given polymer length of ```n``` and the number of possible mtaching units ```u```, the algorithm performs poorly because the entire polymer has to be searched for every reacting unit (```u * n```).

A little more thinking about the problem will reveal that a last in-first out 
data structure like a stack will perform far more optimally. With a stack, each
character will be read from the polymer string left to right.
* If the stack is empty, we place the current unit we are observing onto the stack.
* If the stack is not empty, we peek it, using the array notation ```arr[-1]```, as opposed to using ```.pop()``` as that actually pops the element off of the ```list```. We compare the top of the stack to the current character, if those elements react, then we simply call ```.pop()``` and move onto the next character.
* If the elements do not react, simply place the current character onto the stack.

Using a stack, we are able to achieve ___O(n)___ complexity, only having to go through the polymer string once to react the entire polymer.

## Star 2

For Star 2, we can't assume we know what the character/unit set is, so we create a function
to loop through the original polymer and map every character/unit into a dictionary. From that point we can create polymers that have the full set of units, minus the set
we are evaluating. Then we just react those polymers and count for the smallest one.

## Notes, and things to look into

Finding reacting units via ```ord()``` is fine, using some type of exlusive or 
strategy might be faster, though marginally.

The order of operations and performance for Star 2 can probably be improved. The
answer I've given is thorough and complete, but some deeper analysis would 
probably reveal some shortcuts that can be taken that will provide the same answer.
For example, can we do the reductions on the already reacted polymer, or do we have 
to do it on the original polymer?