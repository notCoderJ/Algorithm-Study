/**
 * 풀이:
 *  자바 스크립트를 연습할겸 한동안 자바 스크립트로 풀어볼 생각이다.
 *
 *  dfs를 이용해서 1열부터 n열까지 이동하며 퀸을 놓을 수 있는지 검사하고,
 *  놓을 수 있다면 현재 퀸을 놓은 위치를 기록해나가는 방식으로 풀었다.
 *
 *  여기서, 퀸을 해당 위치에 놓을 수 있는 조건은 다음 3가지를 만족해야 하는데,
 *  (열은 dfs 수행마다 달라지기 때문에 고려하지 않았다.)
 *  1. 현재 놓을 행에 다른 퀸이 존재하지 않는다.
 *  2. 현재 놓을 위치의 좌측 대각선 상에 다른 퀸이 존재하지 않는다.
 *  3. 현재 놓을 위치의 우측 대각선 상에 다른 퀸이 존재하지 않는다.
 *
 *  1번 조건은 이전에 퀸을 놓은 행들을 기록하면 되니 간단하다.
 *  그럼, 좌우 대각선은 어떻게 고려할 것인가?
 *  n = 3인 체스판을 예로 들어 살펴보자.
 *    (0,0) (0,1) (0,2)
 *    (1,0) (1,1) (1,2)
 *    (2,0) (2,1) (2,2)
 *
 *  위 예시로부터 다음과 같은 규칙성을 발견할 수 있다.
 *  1. 같은 좌측 대각선(\)에 포함되는 위치는 "행 - 열"의 값이 서로 동일하다.
 *      ex) (0, 0), (1, 1), (2, 2) => 차는 모두 0
 *  2. 같은 우측 대각선(/)에 포함되는 위치는 "행 + 열"의 값이 서로 동일하다.
 *      ex) (0, 2), (1, 1), (2, 0) => 합은 모두 2
 *
 *  위 규칙성을 통해 각 대각선의 방문 기록을 작성해나가면 현재 퀸을 놓을 위치에 다른 퀸이 놓여있는지 확인할 수 있다.
 *  이때, 대각선의 수는 중앙 대각선을 기준으로 좌우 대칭이기 때문에 각 방문 리스트(대각선)의 크기는 간단히 2n개로 설정해주었다.
 *  여기서, 주의할 점이 하나 있는데 우측 대각선의 경우 행과 열의 합이므로 양수가 보장되지만 좌측 대각선은 양수가 보장되지 않는다.
 *  따라서, 이를 보정하기 위해 좌측 대각선의 경우 "행 - 열"에 n - 1을 더해주었다.
 */

const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(path).toString();

const n = parseInt(input);
let answer = 0;
const row = Array(n).fill(false);
const lDiag = Array(2 * n).fill(false);
const rDiag = Array(2 * n).fill(false);

function dfs(col) {
  if (col === n) {
    answer++;
    return;
  }

  for (let i = 0; i < n; i++) {
    if (!row[i] && !lDiag[i - col + n - 1] && !rDiag[i + col]) {
      row[i] = true;
      lDiag[i - col + n - 1] = true;
      rDiag[i + col] = true;
      dfs(col + 1);
      row[i] = false;
      lDiag[i - col + n - 1] = false;
      rDiag[i + col] = false;
    }
  }
}

dfs(0);

console.log(answer);
