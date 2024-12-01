import { readPuzzleInput, InputFile } from './readFile';
import { readFileSync } from 'fs';

jest.mock('fs');

describe('readPuzzleInput', () => {
  it('should read and parse the example file correctly', () => {
    const mockFileContent = 'line1\nline2\nline3\n';
    (readFileSync as jest.Mock).mockReturnValue(mockFileContent);

    const result = readPuzzleInput(InputFile.EXAMPLE);

    expect(result).toEqual(['line1', 'line2', 'line3']);
    expect(readFileSync).toHaveBeenCalledWith('example.txt', 'utf-8');
  });

  it('should read and parse the input file correctly', () => {
    const mockFileContent = 'lineA\nlineB\nlineC\n';
    (readFileSync as jest.Mock).mockReturnValue(mockFileContent);

    const result = readPuzzleInput(InputFile.INPUT);

    expect(result).toEqual(['lineA', 'lineB', 'lineC']);
    expect(readFileSync).toHaveBeenCalledWith('input.txt', 'utf-8');
  });

  it('should ignore empty lines and trim spaces', () => {
    const mockFileContent = ' line1 \n\n line2 \n\n';
    (readFileSync as jest.Mock).mockReturnValue(mockFileContent);

    const result = readPuzzleInput('anyfile.txt');

    expect(result).toEqual(['line1', 'line2']);
    expect(readFileSync).toHaveBeenCalledWith('anyfile.txt', 'utf-8');
  });
});
