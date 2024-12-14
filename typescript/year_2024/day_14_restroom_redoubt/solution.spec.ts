import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { partOne, partTwo } from './solution';

describe('TestDay14', () => {
  const exampleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe('Part one', () => {
    it('should return correct answer for the example input', () => {
      const result = partOne(exampleInput, 11, 7);
      expect(result).toBe('12');
    });

    it('should return correct answer for the real input', () => {
      const result = partOne(input, 101, 103);
      expect(result).toBe('221655456');
    });
  });

  describe('Part two', () => {
    it('should return correct answer for the real input', () => {
      const result = partTwo(input, 101, 103);
      expect(result).toBe('7858');
    });
  });
});
