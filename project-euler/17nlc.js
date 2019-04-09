//stole this from a very nice anonymous person, i hate myself
const onesAndTeens = [
    0, //nobody says "thirty-zero"
    "one".length,
    "two".length,
    "three".length,
    "four".length,
    "five".length,
    "six".length,
    "seven".length,
    "eight".length,
    "nine".length,
    "ten".length,
    "eleven".length,
    "twelve".length,
    "thirteen".length,
    "fourteen".length,
    "fifteen".length,
    "sixteen".length,
    "seventeen".length,
    "eighteen".length,
    "nineteen".length,
];

const tens = [
    NaN, //"zeroty" is an invalid reference
    NaN, //"onety" is an invalid reference
    "twenty".length,
    "thirty".length,
    "forty".length,
    "fifty".length,
    "sixty".length,
    "seventy".length,
    "eighty".length,
    "ninety".length,
];

const letterLength = (num) => {
    if (num < 20) {
        return onesAndTeens[num];
    } if (num < 100) {
        return tens[Math.floor(num / 10)] + letterLength(num % 10);
    } if (num % 100 === 0) { //special case required because "hundred" !== "hundredand"
        return onesAndTeens[Math.floor(num / 100)] + "hundred".length
    }
    return onesAndTeens[Math.floor(num / 100)] + "hundredand".length + letterLength(num % 100);
};

console.log(
    [...Array(1000).keys()].slice(1) //cheeky javascript way to initialize [1...999]
        .map(letterLength) //get the letter count for each number
        .reduce((sum, cur) => sum + cur) //add them together
        + "onethousand".length //special case
);
