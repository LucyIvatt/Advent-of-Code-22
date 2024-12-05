export const count = <T extends string | number>(array: T[]): Record<T, number> => {
  const counter: Record<T, number> = {} as Record<T, number>;
  array.forEach((item) => {
    counter[item] = (counter[item] || 0) + 1;
  });
  return counter;
};
