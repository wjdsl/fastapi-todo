# TODO 리스트

우아한 멘토링 - 만들면서 익히는 개발지식

- AI 사용 무관, 사용하는 언어에 상관없이 구현 가능
- 구현 후 어떤 점을 중점으로 구현했는지 문서화, 문서화 양식은 자유

## 요구사항
- TODO 리스트 생성
    - 어떤 TODO 리스트인지 알아볼 수 있어야 함.
    - 생성날짜를 알 수 있어야함.
- TODO 생성
    - TODO 이름 설정이 필요.
    - TODO에 대한 설명을 선택적으로 작성할 수 있어야함.
- TODO 수정
    - 이름 수정이 가능해야함.
    - 설명 수정이 가능해야함.
- TODO 체크
    - TODO 완료를 가능하게 해야함.
    - TODO 완료 일시를 확인할 수 있어야함.
- TODO 체크 해제
    - TODO 완료를 취소 가능하게 해야함.
    - TODO 완료 취소시 완료 일시는 무의미한 값이 되어 제외해야함.
- TODO 삭제
    - 생성한 TODO를 제거 가능하게 해야함.

---

# 구현 내용

## 구현 기능

- TODO 리스트 생성
- TODO 생성
- TODO 수정
- TODO 완료
- TODO 완료 취소
- TODO 삭제

## 구현 시 중점적으로 생각한 점

### 1. REST API 설계

REST API 스타일을 고려하여 리소스 중심으로 엔드포인트를 설계했습니다.

- `POST /todo-lists`
- `POST /todo-lists/{list_id}/todos`
- `PATCH /todos/{todo_id}`
- `POST /todos/{todo_id}/complete`
- `POST /todos/{todo_id}/uncomplete`
- `DELETE /todos/{todo_id}`

### 2. 요청과 응답 모델 분리

Pydantic의 `BaseModel`을 사용하여 요청과 응답 모델을 분리했습니다.
클라이언트는 필요한 데이터만 전달하고, `id`, `created_at`, `completed_at`과 같은 값은 서버에서 생성하도록 구현했습니다.

### 3. 예외 처리

존재하지 않는 TODO 리스트 또는 TODO에 접근하는 경우 `404 Not Found`를 반환하도록 구현했습니다.

### 4. 데이터 저장 방식

과제의 핵심 요구사항 구현에 집중하기 위해 Python Dictionary를 사용한 인메모리 저장 방식으로 구현했습니다.
현재 구현은 서버가 재시작되면 데이터가 초기화됩니다.

---

# 실행 방법

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

서버 실행 후 아래 주소에서 Swagger UI를 통해 API를 테스트할 수 있습니다.

```
http://127.0.0.1:8000/docs
```

---

## API 목록

| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | /todo-lists | TODO 리스트 생성 |
| POST | /todo-lists/{list_id}/todos | TODO 생성 |
| PATCH | /todos/{todo_id} | TODO 수정 |
| POST | /todos/{todo_id}/complete | TODO 완료 |
| POST | /todos/{todo_id}/uncomplete | TODO 완료 취소 |
| DELETE | /todos/{todo_id} | TODO 삭제 |

