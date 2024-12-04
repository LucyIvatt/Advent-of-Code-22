import { runPuzzle } from './runPuzzle';
import { functionTimer } from './time';

jest.mock('./time');

describe('runPuzzle', () => {
  const mockFunctionTimer = functionTimer as jest.MockedFunction<typeof functionTimer>;

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should log the correct output and time for both parts', () => {
    const consoleLogSpy = jest.spyOn(console, 'log').mockImplementation(() => {});
    const partOneMock = jest.fn().mockReturnValue('Part One Result');
    const partTwoMock = jest.fn().mockReturnValue('Part Two Result');

    const puzzleInput = ['input1', 'input2'];

    mockFunctionTimer.mockReturnValueOnce({ output: 'Part One Result', time: '0.123' });
    mockFunctionTimer.mockReturnValueOnce({ output: 'Part Two Result', time: '0.456' });

    runPuzzle('1', 'Test Day', partOneMock, partTwoMock, puzzleInput);

    expect(mockFunctionTimer).toHaveBeenCalledWith(partOneMock, puzzleInput);
    expect(mockFunctionTimer).toHaveBeenCalledWith(partTwoMock, puzzleInput);

    expect(consoleLogSpy).toHaveBeenCalledWith('--------------------------------------');
    expect(consoleLogSpy).toHaveBeenCalledWith('Day 1: Test Day');
    expect(consoleLogSpy).toHaveBeenCalledWith('--------------------------------------');
    expect(consoleLogSpy).toHaveBeenCalledWith('Part One Answer: Part One Result - [0.123 seconds]');
    expect(consoleLogSpy).toHaveBeenCalledWith('Part Two Answer: Part Two Result - [0.456 seconds]');
    expect(consoleLogSpy).toHaveBeenCalledWith('--------------------------------------');

    consoleLogSpy.mockRestore();
  });
});
