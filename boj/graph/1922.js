/**
 * 풀이
 *  모든 컴퓨터를 연결하기 위한 최소 비용을 구하는 문제로 크루스칼 알고리즘을 사용하여 풀었다.
 *  1. 주어진 컴퓨터들의 연결 정보를 비용을 기준으로 오름차 정렬한다.
 *  2. 각 자신의 컴퓨터 번호를 부모 컴퓨터 번호로 하여 연결 정보 테이블을 초기화한다.
 *  3. 현재 자신의 루트 컴퓨터 번호를 찾는 find 연산과 두 컴퓨터의 루트 컴퓨터 번호를 비교하여 연결하는 union연산을 정의한다.
 *    3-1. find 연산 수행 시 현재 컴퓨터 번호와 부모 컴퓨터 번호가 일치하지 않으면 부모 컴퓨터를 루트 컴퓨터 번호로 변경해준다.
 *    3-2. union 연산 수행 시 두 컴퓨터의 루트 컴퓨터 번호를 비교하여 더 작은 번호로 테이블을 갱신해준다.
 *  4. 주어진 컴퓨터 연결 정보를 순회하며 3번에 정의한 union연산을 수행하고 사이클이 발생하지 않는 경우만 연결 비용을 누적한다.
 */

const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(path).toString().replaceAll('\r', '').split('\n');

const n = parseInt(input[0]);
const m = parseInt(input[1]);
const graph = [...Array(m)]
  .map((_, i) => input[i + 2].split(' ').map((x) => parseInt(x)))
  .sort((a, b) => a[2] - b[2]);

function print(...msg) {
  console.log(...msg);
}

function Kruskal(n) {
  const parents = [...Array(n + 1)].map((_, i) => i);

  this.find = function (node) {
    if (node !== parents[node]) {
      parents[node] = this.find(parents[node]);
    }
    return parents[node];
  };

  this.union = function (node1, node2) {
    const rootNode1 = this.find(node1);
    const rootNode2 = this.find(node2);

    if (rootNode1 === rootNode2) {
      return false;
    } else if (rootNode1 > rootNode2) {
      parents[rootNode1] = parents[rootNode2];
    } else {
      parents[rootNode2] = parents[rootNode1];
    }
    return true;
  };
}

const kruskal = new Kruskal(n);
const answer = graph.reduce((total, connection) => {
  const [a, b, c] = connection;
  if (kruskal.union(a, b)) {
    return total + c;
  }
  return total;
}, 0);
print(answer);
