export const count = <T extends string | number>(array: T[]): Record<T, number> => {
  const counter: Record<T, number> = {} as Record<T, number>;
  array.forEach((item) => {
    counter[item] = (counter[item] || 0) + 1;
  });
  return counter;
};

export function* generateCombinations(allowedCharacters: string[], length: number): Generator<string> {
  if (length === 0) {
    yield '';
    return;
  }

  for (const char of allowedCharacters) {
    for (const smallerCombination of generateCombinations(allowedCharacters, length - 1)) {
      yield char + smallerCombination;
    }
  }
}
