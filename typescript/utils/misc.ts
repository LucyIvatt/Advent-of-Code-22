/**
 * Counts the occurrences of each unique element in an array.
 *
 * @param array - An array of strings or numbers to be counted.
 * @returns A record where each key is a unique element from the array
 * and the value is the number of times it appears in the array.
 */
export const count = <T extends string | number>(array: T[]): Record<T, number> => {
  const counter: Record<T, number> = {} as Record<T, number>;
  array.forEach((item) => {
    counter[item] = (counter[item] || 0) + 1;
  });
  return counter;
};

/**
 * Generates all possible combinations of a string of a specified length from a given set of allowed characters.
 *
 * @param allowedCharacters - An array of characters to be used in generating combinations.
 * @param length - The desired length of each generated combination.
 * @returns A generator that yields each combination as a string.
 */
export function* generateCombinations(allowedCharacters: string[], length: number): Generator<string> {
  const stack: string[] = [''];

  while (stack.length) {
    const combination = stack.pop()!;
    if (combination.length === length) {
      yield combination;
    } else {
      for (const char of allowedCharacters) {
        stack.push(combination + char);
      }
    }
  }
}
