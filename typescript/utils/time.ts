/**
 * Measures the execution time of a given function and returns the result along with the time taken.
 *
 * @param fn - The function to be timed. It can be either synchronous or asynchronous and should take an array of strings as input and return a string or a promise that resolves to a string.
 * @param input - The input array of strings to be passed to the function.
 * @returns A promise that resolves to an object containing the output of the function and the time taken to execute it in seconds, formatted to three significant digits.
 */
export const functionTimer = async (fn: (...args: string[][]) => string | Promise<string>, ...args: string[][]) => {
  const start = performance.now();
  const output = await fn(...args);
  const end = performance.now();

  return { output, time: Number((end - start) / 1000).toPrecision(3) };
};

/**
 * Delays the execution for a given number of milliseconds.
 *
 * @param ms - The number of milliseconds to delay.
 * @returns A promise that resolves after the specified delay.
 */
export const delay = (ms: number) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};
