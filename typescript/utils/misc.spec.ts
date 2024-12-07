import { count, generateCombinations } from './misc';

describe('misc', () => {
  describe('count', () => {
    it('should correctly count the number of items in a list', () => {
      const inputList = [1, 5, 4, 3, 4, 1, 1];

      expect(count(inputList)).toStrictEqual({ 1: 3, 5: 1, 4: 2, 3: 1 });
    });
  });

  describe('generateCombinations', () => {
    it('should generate all possible combinations given allowed characters and length', () => {
      const allowedCharacters = ['a', 'b'];
      const length = 2;

      const combinations = Array.from(generateCombinations(allowedCharacters, length));

      expect(combinations.sort()).toEqual(['aa', 'ab', 'ba', 'bb'].sort());
    });
  });
});
