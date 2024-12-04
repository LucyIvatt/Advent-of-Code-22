import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { partOne, partTwo } from './solution';

describe('TestDay04', () => {
  const exampleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe('Part one', () => {
    it('should return correct answer for the example input', () => {
      const result = partOne(exampleInput);
      expect(result).toBe('18');
    });

    it('should return correct answer for the real input', () => {
      const result = partOne(input);
      expect(result).toBe('2406');
    });
  });

  describe('Part two', () => {
    it('should return correct answer for the example input', () => {
      const result = partTwo(exampleInput);
      expect(result).toBe('9');
    });

    it('should return correct answer for the real input', () => {
      const result = partTwo(input);
      expect(result).toBe('1807');
    });
  });
});
