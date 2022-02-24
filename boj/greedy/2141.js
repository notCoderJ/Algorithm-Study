/*
  풀이
    자바스크립트 코테에 익숙해질겸 자바스크립트 버전으로 다시 풀어봤다.
    파이썬 코드와 달리 투포인터를 사용하지 않고 중간값을 기준으로 비교하는 방식으로 풀었다.

    자바스크립트로 입력을 받아본 적이 없어서 입력방법 찾기부터 시작해서...
    sort의 동작 방식이 파이썬과 달라 틀린 이유를 찾지 못해 한참을 해맸다ㅠ
    자바스크립트 너란 녀석...
    (sort 동작 방식에 대해 한번 찾아봐야것다. 이전에 Tim sort라는 방식을 사용하는데 복잡하다고 했던 기억이...)

    추가로, 자바스크립트 입력에는 2가지 방식이 있었다.(빠른 성능이 필요한 때는 fs를 쓰자!)
    1. fs 모듈을 사용하는 방법
      fs모듈의 readFileSync를 사용해서 stdin 표준 입력 파일로부터 사용자 입력 데이터를 받아오는 방식이다.
      Sync가 붙어 있듯이 동기적으로 동작하기 때문에 입력을 받는 동안 다른 코드가 실행되지 않는다.

      사용 방법은 아래와 같다.
      const fs = require('fs') // 모듈을 로드해주고
      const input = fs.readFileSync('/dev/stdin').toString().split(입력 구분자) // 이와 같은 형태로 입력을 받아오면 된다.

      여기서, window 상에서 vscode로 테스트하고 싶다면
      "npm install fs"로 먼저 fs 모듈을 설치해주고
      최상위 경로에 txt파일을 생성한 후 입력할 데이터를 작성해주고 readFileSync 함수의 인자로 '/dev/stdin' 대신 해당 파일 이름을 넣어주면 된다.

    2. readline 모듈을 사용하는 방법
      const readline = require('readline'); // readline 모듈을 로드해주고
      
      // 입출력 인터페이스를 설정한다.
      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
      });

      // 해당 인터페이스에 이벤트 핸들러를 달아준다.
      rl.on('line', (line) => {
        console.log(line);

        // 입력을 종료할 때 작성
        rl.close() // 만약, 여러줄 입력이 필요할 경우 close를 빼고 외부에 빈 리스트를 하나 생성한 후 입력 값들을 넣어줘야 한다.
      }).on('close', () => {
        process.exit();
      });
*/

// 입력 시간 초과 시 사용
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(path).toString().split('\n');

const n = parseInt(input[0]);
const town = [];
for (let i = 1; i < n + 1; i++) {
  town.push(input[i].split(' ').map((data) => parseInt(data)));
}

const solution = (n, town) => {
  const sortedTown = town.sort((a, b) => a[0] - b[0]);
  const totalCnt = town.reduce((prev, [_, cnt]) => prev + cnt, 0);
  let midVal = Math.ceil(totalCnt / 2);

  for (let i = 0; i < n; i++) {
    midVal -= sortedTown[i][1];
    if (midVal <= 0) {
      console.log(sortedTown[i][0]);
      return;
    }
  }
};

solution(n, town);
