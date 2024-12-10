export class IndexRange {
  value: number;
  left: number;
  right: number;

  constructor(id: number, left: number, right: number) {
    this.value = id;
    this.left = left;
    this.right = right;
  }

  getLength = () => {
    if (this.left > this.right) return 0;
    return this.right - this.left + 1;
  };
  toString = () => `{value:${this.value}, range:[${this.left}, ${this.right}], length:${this.getLength()}}`;
  updateRange = (left: number, right: number) => {
    this.left = left;
    this.right = right;
  };
}
