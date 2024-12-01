export const functionTimer = (fn: (input: string[]) => string, input: string[]) => {
  const start = performance.now();
  const output = fn(input);
  const end = performance.now();

  return { output, time: (end - start).toFixed(5) };
};
