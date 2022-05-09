/**
 * 풀이
 *  어떤 위치에서 출발하여 특정 위치에 빠르게 도착하는 유형의 문제로 bfs를 사용하여 풀었다.
 *  현재 위치에서 U, D 방향으로 각각 이동하는 위치가 허용 범위 내에 있으면
 *  다음 위치를 방문 처리한 후 (다음 위치, 현재 버튼 클릭 수 + 1)을 큐에 넣는다.
 *  큐에서 각 위치를 하나씩 꺼내면서 위 작업을 반복한다.
 *  만약, 큐에서 꺼낸 현재 위치가 G라면 현재 버튼 클릭 수를 반환하고,
 *  큐가 빌 때까지 G층에 도달하지 못한다면 'use the stairs'를 반환한다.
 */

const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs
  .readFileSync(path)
  .toString()
  .split(' ')
  .map((val) => parseInt(val));

function print(...message) {
  console.log(...message);
}

const [F, S, G, U, D] = input;

function solution(F, S, G, U, D) {
  const visited = Array(F + 1).fill(false);
  visited[S] = true;
  const q = [[S, 0]];

  while (q.length !== 0) {
    [current, cnt] = q.shift();
    if (current === G) {
      return cnt;
    }

    [U, -D].forEach((move) => {
      const next = current + move;
      if (0 < next && next <= F && !visited[next]) {
        visited[next] = true;
        q.push([next, cnt + 1]);
      }
    });
  }

  return 'use the stairs';
}

print(solution(F, S, G, U, D));
