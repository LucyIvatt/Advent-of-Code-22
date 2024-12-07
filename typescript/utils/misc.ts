export const count = <T extends string | number>(array: T[]): Record<T, number> => {
  const counter: Record<T, number> = {} as Record<T, number>;
  array.forEach((item) => {
    counter[item] = (counter[item] || 0) + 1;
  });
  return counter;
};

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
