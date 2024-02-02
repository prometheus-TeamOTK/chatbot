- 캐릭터 채팅(class Character)
    - def __init __(self, file_path, user, relation, situation)
        - file_path: 캐릭터 파일 패스(봇 캐릭터의 설정 - 캐릭터 이름.json 파일로 제공)
            - 이거 사용자 인풋 받고 저장해 둘 것
        - user: 사용자 캐릭터(사용자가 캐릭터와 대화 시 사용할 캐릭터)
        - relation: 사용자 캐릭터와 봇 캐릭터의 관계(따로 파일 제공 예정)
        - situation: 사용자 캐릭터, 봇 캐릭터와 대화하는 상황(따로 파일 제공 예정)
    - 프롬프트 입력해서 대화 가져오기: receive_chat()

- 대화 내역 저장
    - 지금은 스트림릿 session 그거 메세지 통으로 저장하는데 지금 하는 건 디비 연결해야 되나…? 잘 모름 여튼 json 형식으로 누가 보내는지, 문장은 뭔지 같이 저장하면 됨

- 대화 요약(class Summary)
    - def __init __(self, chatting_file, situation)
        - chatting_file: 대화 내역 저장한 파일
        - situation: 캐릭터 채팅에 넣어 준 거 그대로 넣어 주면 됨
    - 대화 요약하기: summary()

- 그림 생성
    - 넘겨 줄 데이터: 사용자 인풋으로 받은 대화할 캐릭터, user, summary() 결과값