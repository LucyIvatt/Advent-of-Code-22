import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { partOne, partTwo } from './solution';

describe('TestDay18', () => {
  const exampleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe('Part one', () => {
    it('should return correct answer for the example input', () => {
      const result = partOne(exampleInput, 7, 12);
      expect(result).toBe('22');
    });

    it('should return correct answer for the real input', () => {
      const result = partOne(input, 71, 1024);
      expect(result).toBe('340');
    });
  });

  describe('Part two', () => {
    it('should return correct answer for the example input', () => {
      const result = partTwo(exampleInput, 7);
      expect(result).toBe('6,1');
    });

    it('should return correct answer for the real input', () => {
      const result = partTwo(input, 71);
      expect(result).toBe('34,32');
    });
  });
});
