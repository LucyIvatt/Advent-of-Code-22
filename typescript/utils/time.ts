export const functionTimer = (fn: (input: string[]) => string, input: string[]) => {
  const start = performance.now();
  const output = fn(input);
  const end = performance.now();

  return { output, time: Number((end - start) / 1000).toPrecision(3) };
};
