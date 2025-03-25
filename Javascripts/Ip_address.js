// you are to find the number of valid ip addresses that can be formed from the given string

function ipsBetween(start, end) {
    const ipToInt = (ip) => ip
      // Split IP address string by dots into array of numbers
      .split('.')
      // Use reduce to convert the array into a single integer
      .reduce((acc, num) => {
        // For each octet:
        // 1. Multiply accumulator by 256 (shift left by 8 bits)
        // 2. Add current number (converted from string using +)
        // This effectively treats IP as a 32-bit number
        return acc * 256 + +num;
      }, 0); 
    // Calculate difference between end and start IP addresses
    // This gives us the number of IP addresses between them
    return ipToInt(end) - ipToInt(start);
}
//   i spent a long time on this one. i was able to get the solution but i was not able to understand the solution. i will come back to this one later.
// my  solution was very bad and not optimized.so chatgpt suggested this solution.😭😭😭