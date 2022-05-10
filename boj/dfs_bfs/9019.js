/**
 * 풀이
 *  bfs를 사용하여 현재 레지스터 값에서 D, S, L, R 연산을 반복 수행하는 방식으로 풀었다.
 *  1. 큐에 시작 값인 A와 현재까지 명령어인 빈문자열('')을 넣는다.
 *  2. 큐에서 값을 하나 꺼내 현재 값에서 D, S, L, R 연산을 각각 수행한다.
 *  3. 2번 연산 값을 방문한 적 없는 경우 방문 처리 후 (다음 값, 현재까지 명령어 + 연산 명령어)을 큐에 넣는다.
 *  4. 2, 3 과정을 반복하며 현재 값이 B가 되는 경우 현재까지의 명령어를 반환한다.
 */

const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(path).toString().replaceAll('\r', '').split('\n');

function print(...msg) {
  console.log(...msg);
}

const commands = ['D', 'S', 'L', 'R'];
const calculators = [
  (num) => (num * 2) % 10000, // D
  (num) => (num + 9999) % 10000, // S
  (num) => ((num * 10) % 10000) + Math.floor(num / 1000), // L
  (num) => (num % 10) * 1000 + Math.floor(num / 10), // R
];

function solution(a, b) {
  const visited = Array(10000).fill(false);
  visited[a] = true;
  const q = [[a, '']];

  while (q.length !== 0) {
    const [cur, cmd] = q.shift();
    if (cur === b) {
      return cmd;
    }

    calculators.forEach((calcFunc, i) => {
      const next = calcFunc(cur);
      if (!visited[next]) {
        visited[next] = true;
        q.push([next, cmd + commands[i]]);
      }
    });
  }
}

input.slice(1).forEach((ab) => {
  const [a, b] = ab.split(' ').map((num) => parseInt(num));
  print(solution(a, b));
});
