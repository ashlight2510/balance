#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add English translations to QUESTIONS array
This script reads the QUESTIONS array and creates a properly translated version
"""

import re
import json

# Translation mapping - Korean to English
# This is a comprehensive translation of all 200 questions
translations = {
    "평생 물만 마시기 vs 평생 탄산만 마시기": "Drink only water for life vs Drink only carbonated drinks for life",
    "평생 라면 금지 vs 평생 치킨 금지": "No ramen for life vs No chicken for life",
    "평생 커피 금지 vs 평생 초콜릿 금지": "No coffee for life vs No chocolate for life",
    "평생 매운맛만 가능 vs 평생 순한맛만 가능": "Only spicy food for life vs Only mild food for life",
    "평생 밥만 먹기 vs 평생 빵만 먹기": "Only rice for life vs Only bread for life",
    "평생 떡볶이 금지 vs 평생 아이스크림 금지": "No tteokbokki for life vs No ice cream for life",
    "삼겹살 무한 vs 초밥 무한": "Unlimited pork belly vs Unlimited sushi",
    "피자 토핑 전부 빼기 vs 토핑 5개 이상만 가능": "Pizza with no toppings vs Pizza with 5+ toppings only",
    "평생 야식 가능(살 안 찜) vs 평생 야식 금지(살 안 찜)": "Late night snacks allowed (no weight gain) vs No late night snacks (no weight gain)",
    "김치 없이 살기 vs 국물 없이 살기": "Live without kimchi vs Live without soup",
    "짠맛 2배로 느끼기 vs 단맛 2배로 느끼기": "Taste saltiness 2x stronger vs Taste sweetness 2x stronger",
    "평생 콜라만 가능 vs 평생 사이다만 가능": "Only cola for life vs Only sprite for life",
    "아이스크림 겨울에만 가능 vs 여름에만 가능": "Ice cream only in winter vs Ice cream only in summer",
    "치킨은 항상 퍽퍽살 vs 항상 닭다리만(다른 부위 없음)": "Chicken always breast vs Always only drumsticks (no other parts)",
    "라면은 국물만 vs 면만": "Ramen broth only vs Noodles only",
    "햄버거는 패티 2장 vs 치즈 2장(패티 1장)": "Burger with 2 patties vs Burger with 2 cheese (1 patty)",
    "떡볶이는 떡만 vs 어묵만": "Tteokbokki rice cakes only vs Fish cakes only",
    "평생 과일 금지 vs 평생 채소 금지": "No fruits for life vs No vegetables for life",
    "매일 같은 메뉴 vs 매일 랜덤 메뉴(선택 불가)": "Same menu every day vs Random menu every day (can't choose)",
    "외식만 가능 vs 집밥만 가능": "Only eating out vs Only home-cooked meals",
    
    "알람 없이 기상 vs 항상 알람 10개 필요": "Wake up without alarm vs Always need 10 alarms",
    "하루 4시간만 자기 vs 하루 12시간씩 자기": "Sleep only 4 hours a day vs Sleep 12 hours a day",
    "샤워 5분 제한 vs 샤워 물 온도 랜덤": "5-minute shower limit vs Random shower water temperature",
    "평생 휴대폰 배터리 20%에서 멈춤 vs 80%에서 멈춤": "Phone battery stops at 20% for life vs Stops at 80% for life",
    "평생 이어폰 한쪽만 가능 vs 항상 스피커로만 듣기": "Only one earbud for life vs Always listen through speakers only",
    "이불 항상 차가움 vs 항상 따뜻함": "Blanket always cold vs Always warm",
    "비 오는 날만 외출 가능 vs 맑은 날만 외출 가능": "Can only go out on rainy days vs Can only go out on sunny days",
    "평생 신발 끈 자주 풀림 vs 지퍼 자주 걸림": "Shoelaces often come untied for life vs Zipper often gets stuck for life",
    "하루 10분 순간이동 가능 vs 하루 1시간 투명인간 가능": "10 minutes teleportation per day vs 1 hour invisibility per day",
    "항상 5분 늦게 도착 vs 항상 30분 일찍 도착": "Always 5 minutes late vs Always 30 minutes early",
    "집안 온도 항상 18도 vs 항상 28도": "Room temperature always 18°C vs Always 28°C",
    "와이파이만 가능 vs 데이터만 가능": "WiFi only vs Mobile data only",
    "평생 폰 케이스 없이 vs 평생 두꺼운 범퍼만": "No phone case for life vs Only thick bumper case for life",
    "비밀번호 매일 바뀜 vs 비밀번호 절대 못 바꿈": "Password changes every day vs Can never change password",
    "평생 손목시계만 사용 vs 평생 벽시계만 의존": "Only use wristwatch for life vs Only depend on wall clock for life",
    "하루에 딱 한 번만 웃기 vs 하루에 딱 한 번만 화내기": "Laugh only once a day vs Get angry only once a day",
    "평생 모기 한 마리 따라다님 vs 파리 한 마리 따라다님": "One mosquito follows you for life vs One fly follows you for life",
    "평생 택시 금지 vs 평생 지하철 금지": "No taxis for life vs No subway for life",
    "엘리베이터만 가능 vs 계단만 가능": "Elevator only vs Stairs only",
    "양치 30초만 가능 vs 세수 30초만 가능": "Brush teeth for only 30 seconds vs Wash face for only 30 seconds",
    
    "직장/학교에서 매일 발표 vs 매일 단체사진": "Daily presentations at work/school vs Daily group photos",
    "상사/교수님이 농담 강요 vs 칭찬 강요": "Boss/professor forces jokes vs Forces compliments",
    "매일 회의 2시간 vs 매일 보고서 2시간": "2 hours of meetings every day vs 2 hours of reports every day",
    "출근/등교 30분 추가 vs 퇴근/하교 30분 추가": "30 minutes added to commute/school vs 30 minutes added to leaving work/school",
    "팀플만 있는 학기 vs 시험만 있는 학기": "Semester with only team projects vs Semester with only exams",
    "매일 야근 1시간 vs 주말 출근 월 2회": "1 hour overtime every day vs Weekend work 2 times a month",
    "회사 점심 메뉴 항상 랜덤 vs 항상 고정": "Company lunch menu always random vs Always fixed",
    "메일/메신저 답장 즉시 강제 vs 하루 2번만 확인 가능": "Must reply to emails/messages immediately vs Can only check 2 times a day",
    "회식 월 4회 vs 워크숍 분기 1회": "Company dinners 4 times a month vs Workshop once a quarter",
    "발표는 완벽하지만 질문에 약함 vs 발표는 약하지만 질문에 강함": "Perfect at presentations but weak at Q&A vs Weak at presentations but strong at Q&A",
    "월급 10%↑ 대신 휴가 0일 vs 월급 10%↓ 대신 휴가 2배": "10% salary increase but 0 vacation days vs 10% salary decrease but 2x vacation days",
    "출근길 지옥 vs 퇴근길 지옥": "Commute to work is hell vs Commute home is hell",
    "혼자 일하기 vs 계속 협업하기": "Work alone vs Always collaborate",
    "칭찬은 공개적으로만 vs 피드백은 공개적으로만": "Compliments only publicly vs Feedback only publicly",
    "팀원이 너무 느림 vs 팀원이 너무 빠름(나를 끌고 감)": "Teammates too slow vs Teammates too fast (dragging me along)",
    "회의 때만 말 잘함 vs 작업 때만 잘함": "Good at speaking only in meetings vs Good at work only",
    "상사가 디테일 집착 vs 상사가 방향만 던짐": "Boss obsessed with details vs Boss only gives direction",
    "매일 아침 스몰토크 10분 vs 매일 퇴근 전 회고 10분": "10 minutes small talk every morning vs 10 minutes reflection before leaving work",
    "오피스 BGM 강제 vs 완전 무음 강제": "Forced office BGM vs Forced complete silence",
    "자리 고정 오픈오피스 vs 자리 매일 랜덤": "Fixed seat open office vs Random seat every day",
    
    "친구랑 항상 취향 겹침 vs 항상 반대 취향": "Always same taste as friends vs Always opposite taste",
    "답장 빠른 친구만 vs 약속 잘 잡는 친구만": "Only friends who reply fast vs Only friends who make plans well",
    "읽씹은 없음(대신 단답) vs 단답 없음(대신 읽씹)": "No read receipts (but short replies) vs No short replies (but read receipts)",
    "내 얘기만 하는 친구 vs 남 얘기만 하는 친구": "Friends who only talk about themselves vs Friends who only talk about others",
    "생일파티 크게 vs 생일 완전 조용히": "Big birthday party vs Completely quiet birthday",
    "선물 센스 없음 vs 축하 멘트 센스 없음": "No gift sense vs No congratulatory message sense",
    '"사진 많이 찍자" 친구 vs "사진 0장" 친구': "Friends who say 'let's take many photos' vs Friends who take 0 photos",
    "만날 때마다 계획 빡세게 vs 만날 때마다 즉흥": "Strict plans every time we meet vs Impromptu every time we meet",
    "단톡방 활발 vs 단톡방 조용(필요할 때만)": "Active group chat vs Quiet group chat (only when needed)",
    "친구가 약속 10분 늦음 vs 내가 10분 늦음": "Friend is 10 minutes late vs I am 10 minutes late",
    "친해지면 드립 심함 vs 친해지면 무뚝뚝": "More jokes when close vs More blunt when close",
    "매일 연락하는 관계 vs 일주일에 한 번 깊게 대화": "Relationship with daily contact vs Deep conversation once a week",
    "취미 같이 하는 친구 vs 고민 들어주는 친구": "Friends who share hobbies vs Friends who listen to worries",
    "말로 애정표현 vs 행동으로 애정표현": "Express affection with words vs Express affection with actions",
    "데이트는 항상 야외 vs 항상 실내": "Dates always outdoors vs Always indoors",
    "고백은 먼저 하기 vs 고백은 받기": "Confess first vs Receive confession",
    "연애 중 SNS 공개 vs 비공개": "Public SNS during relationship vs Private SNS",
    "기념일 챙기기 빡세게 vs 기념일 아예 안 챙기기": "Strictly remember anniversaries vs Never remember anniversaries",
    "싸우면 바로 풀기 vs 하루 지나서 풀기": "Resolve fights immediately vs Resolve after a day",
    "여행은 둘이만 vs 친구 커플까지 넷이": "Travel just the two of us vs Travel with friend couple (four of us)",
    
    "하루 1번 미래 10초 보기 vs 과거 10초 보기": "See 10 seconds into future once a day vs See 10 seconds into past once a day",
    "마음 읽기(확률 50%) vs 거짓말 감지(확률 90%)": "Read minds (50% chance) vs Detect lies (90% chance)",
    "순간이동(1일 3회) vs 시간 멈춤(1일 10초)": "Teleportation (3 times a day) vs Stop time (10 seconds a day)",
    "투명인간 vs 동물과 대화": "Invisibility vs Talk to animals",
    "초능력 있는데 남이 모름 vs 초능력 없는데 모두 믿음": "Have superpower but others don't know vs No superpower but everyone believes",
    "원하는 꿈 꾸기 vs 꿈 없이 깊게 자기": "Dream what you want vs Sleep deeply with no dreams",
    "평생 운이 좋음(실력 0) vs 실력 좋음(운 0)": "Lucky for life (skill 0) vs Skilled for life (luck 0)",
    "매일 1만원 랜덤 획득 vs 주 1회 10만원 확정 획득": "Randomly get 10,000 won daily vs Definitely get 100,000 won once a week",
    "말하면 현실이 됨(하루 1문장) vs 생각하면 현실이 됨(하루 1생각)": "What you say becomes reality (1 sentence a day) vs What you think becomes reality (1 thought a day)",
    "어디서든 길 안 잃음 vs 누구와도 금방 친해짐": "Never get lost anywhere vs Quickly become friends with anyone",
    "하루 30분 공중부양 vs 하루 30분 초고속 달리기": "30 minutes levitation per day vs 30 minutes super-speed running per day",
    "손대면 고장 고치기 vs 손대면 깨끗해지기": "Fix broken things by touching vs Clean things by touching",
    "내가 한 선택 항상 정답 vs 내가 피한 선택이 정답": "My choices are always correct vs Choices I avoid are correct",
    "원하는 사람과 10분 대화 vs 원하는 장소에 10분 체류": "10-minute conversation with desired person vs 10-minute stay at desired place",
    "평생 다이어트 필요 없음 vs 평생 감기 안 걸림": "Never need to diet for life vs Never catch a cold for life",
    "나만 자막 보임 vs 나만 배경음악 들림": "Only I see subtitles vs Only I hear background music",
    "기억력 2배 vs 집중력 2배": "2x memory vs 2x concentration",
    "감정 컨트롤 가능 vs 통증 컨트롤 가능": "Control emotions vs Control pain",
    "말발 S급 vs 글발 S급": "S-tier speaking vs S-tier writing",
    "아침형 천재 vs 밤형 천재": "Morning genius vs Night genius",
    
    "평생 여름만 vs 평생 겨울만": "Only summer for life vs Only winter for life",
    "여행은 바다만 vs 산만": "Travel only to beaches vs Only to mountains",
    "국내여행만 vs 해외여행만(1년에 1번)": "Only domestic travel vs Only international travel (once a year)",
    "혼자 여행만 vs 무조건 단체여행": "Only solo travel vs Always group travel",
    "비행기만 가능 vs 기차만 가능": "Plane only vs Train only",
    "숙소는 호텔만 vs 게스트하우스만": "Hotels only vs Guesthouses only",
    "계획 100% 세우기 vs 계획 0% 즉흥": "100% planning vs 0% planning (impromptu)",
    "사진 1,000장 찍기 vs 사진 0장": "Take 1,000 photos vs Take 0 photos",
    "관광지 필수 vs 맛집 필수": "Must visit tourist spots vs Must visit famous restaurants",
    "짧게 자주 여행 vs 길게 가끔 여행": "Short frequent trips vs Long occasional trips",
    "캠핑만 가능 vs 글램핑만 가능": "Camping only vs Glamping only",
    "여행 중 쇼핑 금지 vs 여행 중 카페 금지": "No shopping during travel vs No cafes during travel",
    "여행 중 길 잃기 vs 여행 중 비 맞기": "Get lost during travel vs Get caught in rain during travel",
    "여행 중 배탈 vs 여행 중 휴대폰 고장": "Stomach trouble during travel vs Phone breaks during travel",
    "여행은 힐링 vs 여행은 액티비티": "Travel for healing vs Travel for activities",
    "새벽 출발 vs 밤 도착": "Early morning departure vs Night arrival",
    "유명한 곳만 vs 아무도 모르는 곳만": "Only famous places vs Only unknown places",
    "여행 내내 혼자 식사 vs 여행 내내 단체 식사": "Eat alone throughout trip vs Group meals throughout trip",
    "짐 가볍게(불편) vs 짐 무겁게(편함)": "Light luggage (inconvenient) vs Heavy luggage (convenient)",
    "여행 경비 2배(동행 불가) vs 여행 경비 반(동행 가능)": "2x travel expenses (no companion) vs Half travel expenses (companion allowed)",
    
    "게임은 스토리형 vs 경쟁형": "Story-based games vs Competitive games",
    "롤/오버워치 같은 팀게임만 vs 싱글게임만": "Only team games like LoL/Overwatch vs Only single-player games",
    "하루 1시간만 게임 vs 주말에 몰아 게임": "Game only 1 hour a day vs Binge game on weekends",
    "게임할 때 음성채팅 필수 vs 채팅 금지": "Voice chat required when gaming vs No chat when gaming",
    "승부욕 강한 파티 vs 웃긴 파티": "Competitive party vs Funny party",
    "랭크만 vs 일반만": "Ranked only vs Casual only",
    "키보드 소리 큰 기계식 vs 조용한 멤브레인": "Loud mechanical keyboard vs Quiet membrane keyboard",
    "콘솔만 vs PC만": "Console only vs PC only",
    "모바일게임만 vs 보드게임만": "Mobile games only vs Board games only",
    "게임할 때 간식 금지 vs 음료 금지": "No snacks when gaming vs No drinks when gaming",
    "영화는 극장만 vs 집에서만": "Movies only in theaters vs Only at home",
    "드라마 정주행만 vs 매주 본방만": "Only binge-watching dramas vs Only watching live broadcasts weekly",
    "스포 당하기 vs 결말 미루기": "Get spoiled vs Delay ending",
    "책 종이책만 vs 전자책만": "Only physical books vs Only e-books",
    "음악은 라이브만 vs 음원만": "Only live music vs Only recorded music",
    "노래는 후렴만 반복 vs 1절만 반복": "Only repeat chorus vs Only repeat first verse",
    "춤추기 잘함 vs 노래 잘함": "Good at dancing vs Good at singing",
    "그림 잘 그림 vs 사진 잘 찍음": "Good at drawing vs Good at photography",
    "취미 10개 얕게 vs 취미 1개 깊게": "10 hobbies shallowly vs 1 hobby deeply",
    "혼자 취미 vs 같이 취미": "Hobbies alone vs Hobbies together",
    
    "내 폰 자동수정 항상 이상함 vs 자동완성 항상 스포함": "Phone autocorrect always wrong vs Autocomplete always spoils",
    "인터넷 속도 2배 vs 배터리 2배": "2x internet speed vs 2x battery life",
    "SNS 완전 끊기 vs 유튜브 완전 끊기": "Completely quit SNS vs Completely quit YouTube",
    "광고 없는 대신 월 1만원 vs 무료 대신 광고 2배": "No ads but pay 10,000 won/month vs Free but 2x ads",
    "다크모드만 가능 vs 라이트모드만 가능": "Dark mode only vs Light mode only",
    "키보드 이모지 금지 vs 짤 저장 금지": "No emoji on keyboard vs No meme saving",
    "검색은 항상 1페이지에 정답 vs 검색은 항상 랜덤(대신 신기함)": "Search always shows correct answer on page 1 vs Search always random (but interesting)",
    "지도앱 없기 vs 번역앱 없기": "No map app vs No translation app",
    "폰 분실 한 달 1번 vs 인터넷 끊김 한 달 1번": "Lose phone once a month vs Internet disconnects once a month",
    "사진 자동백업 없음 vs 연락처 자동백업 없음": "No photo auto-backup vs No contact auto-backup",
    "AI가 내 일정 다 관리 vs AI가 내 대화 다 요약(프라이버시 걱정)": "AI manages all my schedule vs AI summarizes all my conversations (privacy concern)",
    "영상통화만 가능 vs 음성통화만 가능": "Video calls only vs Voice calls only",
    "문자만 가능 vs 전화만 가능": "Text only vs Call only",
    "모든 알림 켜짐 강제 vs 모든 알림 꺼짐 강제": "All notifications forced on vs All notifications forced off",
    "비밀번호 없이 얼굴인식만 vs OTP만": "Face recognition only (no password) vs OTP only",
    "폰 카메라 화질 최강 vs 스피커 음질 최강": "Best phone camera quality vs Best speaker sound quality",
    "폰 켜는데 30초 vs 앱 열리는데 10초": "Phone takes 30 seconds to turn on vs Apps take 10 seconds to open",
    "폰 화면 작게만 vs 크게만": "Small phone screen only vs Large phone screen only",
    "인터넷 댓글 절대 못 달기 vs 좋아요 절대 못 누르기": "Can never comment online vs Can never like posts",
    "내 과거 검색기록 공개 vs 내 미래 검색기록 공개": "Past search history public vs Future search history public",
    
    "평생 모자만 쓰기 vs 평생 선글라스만 쓰기": "Only wear hats for life vs Only wear sunglasses for life",
    "매일 같은 옷 vs 매일 랜덤 옷(내가 고른 적 없음)": "Same clothes every day vs Random clothes every day (never chosen by me)",
    "패딩만 입기 vs 코트만 입기": "Only wear padded jackets vs Only wear coats",
    "운동은 유산소만 vs 근력만": "Only cardio exercise vs Only strength training",
    "하루 1만 보 걷기 강제 vs 하루 30분 스트레칭 강제": "Forced to walk 10,000 steps a day vs Forced to stretch 30 minutes a day",
    "살 안 찜(대신 체력 약함) vs 체력 최강(대신 살 잘 찜)": "Don't gain weight (but weak stamina) vs Maximum stamina (but gain weight easily)",
    "키 5cm 더 vs 시력 1.0 평생 유지": "5cm taller vs Maintain 1.0 vision for life",
    "피부 완벽 vs 머리숱 완벽": "Perfect skin vs Perfect hair volume",
    "목소리 좋아짐 vs 손글씨 좋아짐": "Better voice vs Better handwriting",
    "기억력은 나쁨(스트레스 없음) vs 기억력은 좋음(과거 흑역사 선명)": "Bad memory (no stress) vs Good memory (past cringe clear)",
    "웃음소리 크게 들림 vs 한숨소리 크게 들림": "Laugh sounds loud vs Sigh sounds loud",
    "말하면 항상 라임이 맞음 vs 말하면 항상 반말로 들림": "Everything I say rhymes vs Everything I say sounds informal",
    '하루 10번 "헉" 자동 반응 vs 하루 10번 "ㅋㅋ" 자동 반응': "Auto-react 'gasp' 10 times a day vs Auto-react 'lol' 10 times a day",
    "웃긴 드립 자동 생성(가끔 썰렁) vs 분위기 파악 자동(가끔 과몰입)": "Auto-generate funny jokes (sometimes lame) vs Auto-read the room (sometimes over-immersion)",
    "항상 좋은 향기 vs 항상 좋은 촉감(옷/침구)": "Always good scent vs Always good texture (clothes/bedding)",
    "날씨에 민감(기분 좌우) vs 음식에 민감(기분 좌우)": "Sensitive to weather (affects mood) vs Sensitive to food (affects mood)",
    "길거리에서 아는 사람 자주 만남 vs 택배 매일 옴(필요 없는 것도)": "Often meet acquaintances on street vs Packages arrive daily (even unnecessary ones)",
    "지갑 항상 두꺼움(영수증) vs 가방 항상 무거움(잡동사니)": "Wallet always thick (receipts) vs Bag always heavy (junk)",
    "내 방 항상 정리됨(대신 물건 위치 랜덤) vs 내 방 항상 어질러짐(대신 위치 고정)": "Room always organized (but item locations random) vs Room always messy (but locations fixed)",
    "물건 자주 잃어버림 vs 물건 자주 깨뜨림": "Often lose things vs Often break things",
    
    '평생 "예스"만 말하기 vs 평생 "노"만 말하기': "Only say 'yes' for life vs Only say 'no' for life",
    "나만 모두의 말이 0.8배속 vs 나만 모두의 말이 1.5배속": "Only I hear everyone at 0.8x speed vs Only I hear everyone at 1.5x speed",
    "웃음 참기 챌린지 매일 1번 vs 눈물 참기 챌린지 매일 1번": "Hold back laughter challenge once a day vs Hold back tears challenge once a day",
    "모든 농담에 진지하게 답함 vs 모든 질문에 농담으로 답함": "Answer all jokes seriously vs Answer all questions with jokes",
    "소개팅 10번 연속 vs 면접 10번 연속": "10 blind dates in a row vs 10 job interviews in a row",
    "하루 1번 랜덤 칭찬 받기 vs 하루 1번 랜덤 지적 받기": "Receive random compliment once a day vs Receive random criticism once a day",
    "항상 첫인상 S급 vs 항상 오래 보면 S급": "Always S-tier first impression vs Always S-tier after long time",
    "어색함 0(대신 눈치 0) vs 눈치 100(대신 어색함 100)": "Awkwardness 0 (but no social awareness) vs Social awareness 100 (but awkwardness 100)",
    "말실수 자주 vs 행동실수 자주": "Often verbal mistakes vs Often action mistakes",
    "나만 시간 감각 정확 vs 나만 방향 감각 정확": "Only I have accurate time sense vs Only I have accurate direction sense",
    "1년에 딱 한 번 대박 vs 매달 소확행 꾸준": "One big win a year vs Small happiness every month",
    "오늘의 운세 100% 맞음 vs 내일의 날씨 100% 맞음": "Today's fortune 100% accurate vs Tomorrow's weather 100% accurate",
    "내 인생 OST가 들림 vs 내 인생 자막이 보임": "Hear my life OST vs See my life subtitles",
    "감정이 색으로 보임 vs 거짓말이 소리로 들림": "See emotions as colors vs Hear lies as sounds",
    "나만 하루 25시간 vs 나만 하루 23시간": "Only I have 25 hours a day vs Only I have 23 hours a day",
    "내 말이 항상 회자됨 vs 내 행동이 항상 밈이 됨": "My words always become trending vs My actions always become memes",
    '평생 "대박"만 감탄사 vs 평생 "헐"만 감탄사': "Only say 'wow' for life vs Only say 'omg' for life",
    "하루 1번 랜덤 소원(작음) vs 1년에 1번 큰 소원": "Random small wish once a day vs One big wish once a year",
    "내가 찍은 사진은 항상 잘 나옴 vs 남이 찍어준 사진은 항상 잘 나옴": "Photos I take always turn out well vs Photos others take of me always turn out well",
    "지금 당장 10억(대신 기억 1개 삭제) vs 매달 300만 평생(기억 그대로)": "1 billion won right now (but delete 1 memory) vs 3 million won monthly for life (memories intact)"
}

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract QUESTIONS array
match = re.search(r'const QUESTIONS = \[(.*?)\];', content, re.DOTALL)
if not match:
    print("Could not find QUESTIONS array")
    exit(1)

questions_text = match.group(1)

# Parse questions
questions = []
for line in questions_text.split('\n'):
    line = line.strip()
    if not line or line.startswith('//'):
        continue
    # Remove quotes and comma
    line = line.strip(',').strip()
    if line.startswith('"') and line.endswith('"'):
        q_text = line[1:-1]
        questions.append(q_text)

print(f"Found {len(questions)} questions")

# Create output with translations
output = []
for i, q in enumerate(questions):
    en_text = translations.get(q, q)  # Use translation if available, otherwise use Korean
    # Escape quotes in strings
    q_escaped = q.replace('\\', '\\\\').replace('"', '\\"')
    en_escaped = en_text.replace('\\', '\\\\').replace('"', '\\"')
    output.append(f'  {{ ko: "{q_escaped}", en: "{en_escaped}" }}')

# Replace in content
new_questions = 'const QUESTIONS = [\n' + ',\n'.join(output) + '\n];'
new_content = content[:match.start()] + new_questions + content[match.end():]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Converted {len(output)} questions to object format with translations")
print("Done!")
