import { functionTimer } from './time';

describe('functionTimer', () => {
  performance.now = jest
    .fn()
    .mockReturnValueOnce(1000) // Start time
    .mockReturnValueOnce(1012.34); // End time

  it('should return the correct output and time in seconds (3.s.f) for a given function', () => {
    const mockFunction = (input: string[]) => input.join(',');
    const input = ['a', 'b', 'c'];

    const result = functionTimer(mockFunction, input);

    expect(result.output).toBe('a,b,c');
    expect(result.time).toBe('0.0123');
  });
});
