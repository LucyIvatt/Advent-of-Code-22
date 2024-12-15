import path from 'path';
import { InputFile, readPuzzleInput } from '../../utils/readFile';
import { partOne, partTwo } from './solution';

describe('TestDay15', () => {
  const exampleInput = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE));
  const exampleInput2 = readPuzzleInput(path.resolve(__dirname, InputFile.EXAMPLE_2));
  const input = readPuzzleInput(path.resolve(__dirname, InputFile.INPUT));

  describe('Part one', () => {
    it('should return correct answer for the example input', () => {
      const result = partOne(exampleInput);
      expect(result).toBe('2028');
    });

    it('should return correct answer for the 2nd example input', () => {
      const result = partOne(exampleInput2);
      expect(result).toBe('10092');
    });

    it('should return correct answer for the real input', () => {
      const result = partOne(input);
      expect(result).toBe('1568399');
    });
  });

  describe('Part two', () => {
    it('should return correct answer for the example input', () => {
      const result = partTwo(exampleInput);
      expect(result).toBe('Part 2 Answer');
    });

    it('should return correct answer for the real input', () => {
      const result = partTwo(input);
      expect(result).toBe('Part 2 Answer');
    });
  });
});
