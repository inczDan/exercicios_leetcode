// https://leetcode.com/problems/smallest-even-multiple/description/

//solução leetcode

var smallestEvenMultiple = function (n) {
    let i = 1;
    while (true) {
        if (n % 2 == 0) {
            return n
        }
        n = n * i
        i++
    }
};