from llama_cpp import Llama

# Llama 모델 로드
llm = Llama.from_pretrained(
    repo_id="LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF",
    filename="EXAONE-3.5-2.4B-Instruct-BF16.gguf",
)

# 대화 루프
print("LLM과 대화를 시작합니다. '종료'라고 입력하면 대화가 종료됩니다.")
messages = []

while True:
    user_input = input(">> ")  # 사용자 입력
    if user_input.strip().lower() == "종료":
        print("대화를 종료합니다.")
        break

    # 사용자 메시지 추가
    messages.append({"role": "user", "content": user_input})

    # 모델의 응답 생성
    response = llm.create_chat_completion(messages=messages)
    assistant_reply = response.get("choices")[0].get("message").get("content")

    # Llama 응답 출력
    print(assistant_reply)

    # 모델의 응답도 대화 내역에 추가
    messages.append({"role": "assistant", "content": assistant_reply})
