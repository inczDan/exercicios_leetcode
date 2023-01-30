// https://leetcode.com/problems/convert-the-temperature/description/
//Solução leetcode

/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function (celsius) {
    let kelvin = celsius + 273.15;
    let farenheit = (celsius * 1.80) + 32;

    return a = [kelvin, farenheit];
};