# ๐ฐ Elice ์ฝ๋ฉ: ์ฒด์์ ๋ผ๋ฆฌ๋ ฅ ํด์ฆ ์ค '์ปค๋ค๋ ๋ฌธ ๋ฐ์ผ๋ก'

## ๋ฌธ์  ์์ฝ :

    7, 11, 17 ํฌ๊ธฐ์ ์์๋ฅผ ์ด์ฉํด ์ผ์ดํฌ๋ฅผ ๋จน์ ๋ ์ด ์์๋ค์ ์กฐํฉ์ผ๋ก ๋จน์ ์ ์๋ ๊ฐ์ฅ ๋ง์ ์ผ์ดํฌ ์?
    ex) ์ผ์ดํฌ 25๊ฐ๋ 7์ง๋ฆฌ 2๊ฐ, 11์ง๋ฆฌ 1๊ฐ๋ฅผ ์ด์ฉํด ๋ ๋ ๐

> ์ฒ์ ๋ฌธ์ ๋ฅผ ์ ํ์ ๋๋ ์ด๋ป๊ฒ ํ์ด์ผ ํ ์ง ๊ฐ์ด ์ค์ง ์์ ๋ณด๊ธฐ์ ๋ฌธํญ๋ค์ ๋ชจ๋ ํ์ธํด๋ณด๋...๐<br>๊ทธ๋์, ํด์ค์ ์ฐธ๊ณ ํ๋ฉฐ ๋ผ๋ฆฌ์ ์ผ๋ก ์๊ฐํ๋ ๊ณผ์ ์ ์ดํดํ ํ ์ ๋ฆฌํด๋ณด์์ต๋๋ค.<br>

<br>

๋จผ์ , ๋ฌธ์ ๋ฅผ ํ๊ธฐ ์ํด ๋ค์๊ณผ ๊ฐ์ ์๊ฐ์ ํ  ์ ์์ต๋๋ค.

    ์ฃผ์ด์ง ์์๋ก ๋ง๋ค ์ ์๋ ์ต๋ ์๊ฐ ์กด์ฌํ๋ค๋ ๊ฒ์
    ๊ฒฐ๊ตญ, ์ด๋ค ์ N์ด ๋ง๋ค ์ ์๋ ์ต๋ ์๋ผ๋ฉด N + 1, N + 2, ... ์ ๋ชจ๋ ๋ง๋ค ์ ์๋ ์๋ผ๋ ๊ฒ์ด๋ค.

๋ค์์ผ๋ก, ์ ๊ฐ์ ์ด ์ฐธ์ด๋ผ๋ ๊ฒ์ ์ฆ๋ชํ๊ธฐ ์ํด N + 1, N + 2, ... ์ด ๋ชจ๋ ๋ง๋ค ์ ์๋ ์๋ผ๋ ๊ฒ์ ์ฆ๋ชํ๋ฉด ๋ฉ๋๋ค.<br>

์ด์ ๋ํ ์ฆ๋ช์ N + 1์ด ๋ง๋ค ์ ์๋ ์๋ผ๋ฉด 7, 11, 17 ์ค ๊ฐ์ฅ ์์ ์์ธ 7์ ๊ธฐ์ค์ผ๋ก ํ์ฌ N + 7๊น์ง ์ฐ์ํ 7๊ฐ์ ์๊ฐ ๋ชจ๋ ๋ง๋ค ์ ์๋ ์๋ผ๋ฉด ์ฆ๋ช์ด ์๋ฃ๋ฉ๋๋ค.(N + 8๋ถํฐ๋ 7์ด ํ ๋ฒ์ฉ ๋ ์ฌ์ฉ๋ ๊ฒ์ด๋ฏ๋ก)

<br>

> ์ ๋ด์ฉ์ ํ๋ก๊ทธ๋๋ฐ์ผ๋ก ์ฎ๊ฒจ ํ์ธํด๋ด์๋ค!

์ ์๊ณ ๋ฆฌ์ฆ์ 2๊ฐ์ง ๋ฐฉ์์ผ๋ก ๊ตฌํํ  ์ ์์ต๋๋ค.

1. [๋จ์ ๋ฐ๋ณต(iteration)์ ์ด์ฉํ ๋ฐฉ๋ฒ](eating_cake_iteration.py)
2. [๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ์ ์ด์ฉํ ๋ฐฉ๋ฒ](eating_cake_dp.py)

๊ทธ๋ผ, ๋ ๋ฐฉ์ ์ค ์ด๋ค ๊ฒ์ด ๋ ํจ์จ์ ์ผ๊น์?

- ๋ฉ๋ชจ๋ฆฌ ์๋ชจ : 1๋ฒ < 2๋ฒ
- ์ํ ์๊ฐ : 1๋ฒ > 2๋ฒ

2๋ฒ ๋ฐฉ๋ฒ์ ๊ฐ๊ฐ์ ๊ฒฝ์ฐ๋ง๋ค dpํ์ด๋ธ์ ๊ฐ์ ๊ธฐ๋กํ๊ธฐ ๋๋ฌธ์ 1๋ฒ ๋ฐฉ๋ฒ๋ณด๋ค ๋ ๋ง์ ๋ฉ๋ชจ๋ฆฌ๋ฅผ ์ฌ์ฉํ๊ฒ ๋ฉ๋๋ค. ํ์ง๋ง, ์ํ ์๊ฐ ์ธก๋ฉด์์ ๋ณด๋ฉด 1๋ฒ ๋ฐฉ๋ฒ์ ๋์ผํ ์ฐ์ฐ์ ๊ณ์ ๋ฐ๋ณตํ๋ ๋ฐ๋ฉด์ 2๋ฒ ๋ฐฉ๋ฒ์ ๊ฒฝ์ฐ ๊ฐ์ ์ฐ์ฐ์ ๋ํด์๋ dpํ์ด๋ธ์ ๊ธฐ๋กํด๋ ๊ฐ๋ง ์ฐธ์กฐํ๋ฉด ๋๊ธฐ ๋๋ฌธ์ ๋ณด๋ค ๋น ๋ฅธ ์ฐ์ฐ์ด ๊ฐ๋ฅํฉ๋๋ค.
