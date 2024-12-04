/**
 * Measures the execution time of a given function and returns the result along with the time taken.
 *
 * @param fn - The function to be timed. It should take an array of strings as input and return a string.
 * @param input - The input array of strings to be passed to the function.
 * @returns An object containing the output of the function and the time taken to execute it in seconds, formatted to three significant digits.
 */
export const functionTimer = (fn: (input: string[]) => string, input: string[]) => {
  const start = performance.now();
  const output = fn(input);
  const end = performance.now();

  return { output, time: Number((end - start) / 1000).toPrecision(3) };
};
