import { readPuzzleInput, InputFile } from './readFile';
import { readFileSync } from 'fs';

jest.mock('fs');

describe('readPuzzleInput', () => {
  it('should read and parse the a file correctly', () => {
    (readFileSync as jest.Mock).mockReturnValue('line1\nline2\nline3');

    const result = readPuzzleInput(InputFile.EXAMPLE);

    expect(result).toEqual(['line1', 'line2', 'line3']);
    expect(readFileSync).toHaveBeenCalledWith('example.txt', 'utf-8');
  });

  it('should ignore empty lines and trim spaces', () => {
    const mockFileContent = ' line1 \nline2 ';
    (readFileSync as jest.Mock).mockReturnValue(mockFileContent);

    const result = readPuzzleInput('anyfile.txt');

    expect(result).toEqual(['line1', 'line2']);
    expect(readFileSync).toHaveBeenCalledWith('anyfile.txt', 'utf-8');
  });
});
