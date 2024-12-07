import { Direction, Grid, rotate } from './grid';

describe('directions', () => {
  describe('rotate', () => {
    it('should correctly rotate by 45 degree angles', () => {
      expect(rotate(Direction.North, 45)).toBe(Direction.NorthEast);
    });

    it('should throw error if angle not divisible by 45', () => {
      expect(() => rotate(Direction.East, 5)).toThrow();
    });
  });
});

describe('grid', () => {
  let grid: Grid<number>;

  it('should create a grid from a 2D array', () => {
    grid = new Grid([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]);
  });

  it('should throw an error if no elements', () => {
    expect(() => new Grid([[]])).toThrow('Grid must have at least one element.');
  });

  describe('getAdjacent', () => {
    const expectedAdjacentCoords = {
      [Direction.NorthWest]: { value: 1, position: [0, 0] },
      [Direction.North]: { value: 2, position: [0, 1] },
      [Direction.NorthEast]: { value: 3, position: [0, 2] },
      [Direction.West]: { value: 4, position: [1, 0] },
      [Direction.East]: { value: 6, position: [1, 2] },
      [Direction.SouthWest]: { value: 7, position: [2, 0] },
      [Direction.South]: { value: 8, position: [2, 1] },
      [Direction.SouthEast]: { value: 9, position: [2, 2] }
    };

    it('should throw an error if no direction offset can be found', () => {
      expect(() => grid.getAdjacent(0, 0, 'invalid-direction' as Direction)).toThrow(
        `Invalid direction: invalid-direction`
      );
    });

    it('should throw an error if the adjacent coord is out of bounds', () => {
      expect(() => grid.getAdjacent(0, 0, Direction.North)).toThrow(
        `Position out of bounds at [0, 0] moving North to [-1, 0]`
      );
    });

    Object.keys(expectedAdjacentCoords).forEach((direction) => {
      const { value, position } = expectedAdjacentCoords[direction as Direction];

      it(`should return the correct value and position for direction ${direction}`, () => {
        const result = grid.getAdjacent(1, 1, direction as Direction);

        expect(result.value).toBe(value);
        expect(result.position).toEqual(position);
      });
    });
  });

  describe('walk', () => {
    it('should throw an error if length is less than 1', () => {
      expect(() => grid.walk(0, 0, Direction.North, 0)).toThrow('Length must be > 0');
    });

    it('should ignore out of bounds coordinates', () => {
      const { values, positions } = grid.walk(1, 1, Direction.East, 5);

      expect(values).toStrictEqual([5, 6]);
      expect(positions).toStrictEqual([
        [1, 1],
        [1, 2]
      ]);
    });

    it('should correctly walk in a direction', () => {
      const { values, positions } = grid.walk(0, 0, Direction.SouthEast, 3);

      expect(values).toStrictEqual([1, 5, 9]);
      expect(positions).toStrictEqual([
        [0, 0],
        [1, 1],
        [2, 2]
      ]);
    });
  });
});
