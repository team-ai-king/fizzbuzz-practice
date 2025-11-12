# fizzbuzz-practice

Fizzbuzz의 팀단위 연습을 위한 저장소입니다.

## How to Contribute

1. Organization 담당자에게 요청하여 멤버가 됩니다.
2. 팀에 join 후 저장소에서 할 일에 대한 issue를 작성합니다.
3. issue 에 대한 pull request 작성(작업)을 위해 fork를 합니다.(저장소당 한번만 하면 됨)
4. fork한 나의 repo를 clone 합니다.
5. `$ git remote add upstream {팀 레포 주소}`를 하여 업데이트 될 팀의 저장소 주소를 미리 등록합니다.
6. branch를 생성하고 issue에 작성한 대로 작업을 실시합니다.
7. 작업이 모두 끝나면 해당 branch에 push합니다.(`$ git push origin {branch name}`)
8. github에 방문하여 pull request를 생성하고 코드리뷰를 실시합니다.
9. can't automatically merge 가 발생했을 경우, 나의 브랜치들을 최신화 합니다. 이 과정에서 작업중인 브랜치에 충돌이 발생하며 이를 해결하여 다시 push 하면 해소 할 수 있습니다.
10. merge된 pull request를 확인하고 다음 작업을 실시합니다.

## Prerequisites

- git
- python3

## How to start

```shell
$ git clone https://github.com/team-ai-king/fizzbuzz-practice.git
$ cd fizzbuzz-practice
$ python fizzbuzz_{username}.py
```

## Features

- 'fizz' for 3의배수
- 'buzz' for 5의배수
- 'fizzbuzz' for 15의 배수
- i for 나머지 숫자들
