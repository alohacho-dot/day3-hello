# AI Code Assistance Education Landing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 40대 이상 성인을 대상으로 한 AI 코드 어시스턴스 교육 판매용 정적 랜딩페이지를 만들고, 상담 신청(카카오톡) 전환을 일관되게 유도한다.

**Architecture:** 단일 정적 페이지(`index.html`)에 핵심 섹션(히어로, 커리큘럼, 후기, 진행 방식, FAQ, CTA)을 순서대로 배치한다. 기능은 최소 JavaScript(CTA 클릭 추적)만 사용하고, 콘텐츠/구조 검증은 Python `unittest`로 TDD 방식으로 고정한다. 결제는 페이지 내 구현하지 않고 "상담 후 계좌이체" 흐름을 명시한다.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, Python 3 `unittest`

---

## 파일 구조(구현 전 확정)

- 생성: `index.html`
  - 랜딩페이지 단일 엔트리
  - 신뢰형 톤의 콘텐츠, CTA, FAQ, 후기 포함
- 생성: `tests/test_landing_page.py`
  - 페이지 구조/카피/CTA/추적 코드 존재 여부를 검증

## Task 1: 기본 페이지 골격과 첫 실패 테스트

**Files:**
- Create: `tests/test_landing_page.py`
- Create: `index.html`
- Test: `tests/test_landing_page.py`

- [ ] **Step 1: 실패 테스트 작성 (섹션 골격 검증)**

```python
import unittest
from pathlib import Path


class LandingPageTest(unittest.TestCase):
    def read_html(self) -> str:
        return Path("index.html").read_text(encoding="utf-8")

    def test_required_sections_exist(self):
        html = self.read_html()
        required_ids = [
            "hero",
            "curriculum",
            "testimonials",
            "process",
            "faq",
            "final-cta",
        ]
        for section_id in required_ids:
            self.assertIn(f'id="{section_id}"', html)

    def test_consultation_and_payment_flow_text_exists(self):
        html = self.read_html()
        self.assertIn("상담 신청", html)
        self.assertIn("상담 후 계좌이체", html)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: 테스트 실행하여 실패 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: FAIL (`FileNotFoundError: 'index.html'`)

- [ ] **Step 3: 최소 구현 작성 (섹션 뼈대 HTML 생성)**

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AI 코드 어시스턴스 교육</title>
  </head>
  <body>
    <section id="hero">
      <h1>40대 이상 성인을 위한 AI 코드 어시스턴스 교육</h1>
      <a class="js-kakao-cta" href="__KAKAO_CHAT_URL__">상담 신청</a>
    </section>

    <section id="curriculum">
      <h2>프로그램 소개/커리큘럼</h2>
    </section>

    <section id="testimonials">
      <h2>수강생 후기/사례</h2>
    </section>

    <section id="process">
      <h2>진행 방식</h2>
      <p>상담 후 계좌이체로 결제가 진행됩니다.</p>
    </section>

    <section id="faq">
      <h2>자주 묻는 질문</h2>
    </section>

    <section id="final-cta">
      <a class="js-kakao-cta" href="__KAKAO_CHAT_URL__">카카오톡으로 상담 신청</a>
    </section>
  </body>
</html>
```

- [ ] **Step 4: 테스트 재실행하여 통과 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: PASS (2 tests)

- [ ] **Step 5: 커밋**

```bash
git add tests/test_landing_page.py index.html
git commit -m "feat: add landing page skeleton with consultation flow"
```

## Task 2: 커리큘럼/타깃 카피를 TDD로 구체화

**Files:**
- Modify: `tests/test_landing_page.py`
- Modify: `index.html`
- Test: `tests/test_landing_page.py`

- [ ] **Step 1: 실패 테스트 추가 (핵심 카피 검증)**

```python
    def test_target_and_curriculum_copy_exists(self):
        html = self.read_html()
        self.assertIn("40대 이상 성인", html)
        self.assertIn("초급", html)
        self.assertIn("활용", html)
        self.assertIn("실전", html)
        self.assertIn("주간 상담 신청 건수", html)
```

- [ ] **Step 2: 테스트 실행하여 실패 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: FAIL (`AssertionError` for missing curriculum detail/KPI copy)

- [ ] **Step 3: 최소 구현 작성 (커리큘럼/목표 문구 추가)**

```html
<section id="hero">
  <p class="eyebrow">신뢰형 교육 프로그램</p>
  <h1>40대 이상 성인을 위한 AI 코드 어시스턴스 교육</h1>
  <p>복잡한 이론보다 실무와 생활에 바로 적용 가능한 활용법을 배웁니다.</p>
  <p><strong>1차 목표:</strong> 주간 상담 신청 건수 증대</p>
  <a class="js-kakao-cta" href="__KAKAO_CHAT_URL__">상담 신청</a>
</section>

<section id="curriculum">
  <h2>프로그램 소개/커리큘럼</h2>
  <ol>
    <li><strong>초급:</strong> AI 코드 어시스턴트 기본 사용법</li>
    <li><strong>활용:</strong> 반복 업무 자동화와 생산성 개선</li>
    <li><strong>실전:</strong> 실제 업무 시나리오에 적용</li>
  </ol>
</section>
```

- [ ] **Step 4: 테스트 재실행하여 통과 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: PASS (3 tests)

- [ ] **Step 5: 커밋**

```bash
git add tests/test_landing_page.py index.html
git commit -m "feat: add target-focused curriculum and KPI copy"
```

## Task 3: 후기/FAQ/진행 방식을 신뢰 중심으로 완성

**Files:**
- Modify: `tests/test_landing_page.py`
- Modify: `index.html`
- Test: `tests/test_landing_page.py`

- [ ] **Step 1: 실패 테스트 추가 (후기/FAQ/진행 방식 상세 검증)**

```python
    def test_testimonials_and_faq_content_exists(self):
        html = self.read_html()
        self.assertGreaterEqual(html.count("Before"), 2)
        self.assertGreaterEqual(html.count("After"), 2)
        self.assertIn("난이도", html)
        self.assertIn("준비물", html)
        self.assertIn("수강시간", html)
        self.assertIn("환불", html)

    def test_process_flow_mentions_consult_then_transfer(self):
        html = self.read_html()
        self.assertIn("상담 신청 → 학습 진단 → 수강 진행 → 상담 후 계좌이체", html)
```

- [ ] **Step 2: 테스트 실행하여 실패 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: FAIL (`AssertionError` for missing Before/After or FAQ keywords)

- [ ] **Step 3: 최소 구현 작성 (후기/FAQ/진행 방식 콘텐츠 추가)**

```html
<section id="testimonials">
  <h2>수강생 후기/사례</h2>
  <article>
    <h3>수강생 A (40대, 비개발 직군)</h3>
    <p><strong>Before:</strong> 코딩 도구가 낯설어 업무 자동화를 시도하지 못함</p>
    <p><strong>After:</strong> 반복 문서 작업을 AI로 단축해 업무 시간을 절감</p>
  </article>
  <article>
    <h3>수강생 B (50대, 현업 개발자)</h3>
    <p><strong>Before:</strong> 신규 도구 도입이 부담스러워 생산성 정체</p>
    <p><strong>After:</strong> 코드 작성/리뷰 보조로 개발 속도와 정확도 향상</p>
  </article>
</section>

<section id="process">
  <h2>진행 방식</h2>
  <p>상담 신청 → 학습 진단 → 수강 진행 → 상담 후 계좌이체</p>
</section>

<section id="faq">
  <h2>자주 묻는 질문</h2>
  <details><summary>난이도는 어떤가요?</summary><p>비전공자도 이해 가능한 난이도로 구성됩니다.</p></details>
  <details><summary>준비물은 무엇인가요?</summary><p>노트북과 인터넷 환경만 있으면 됩니다.</p></details>
  <details><summary>수강시간은 어떻게 되나요?</summary><p>상담 시 일정과 학습 속도에 맞춰 조정합니다.</p></details>
  <details><summary>환불 기준은 어떻게 되나요?</summary><p>상담 시 사전 안내한 기준에 따라 적용됩니다.</p></details>
</section>
```

- [ ] **Step 4: 테스트 재실행하여 통과 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: PASS (5 tests)

- [ ] **Step 5: 커밋**

```bash
git add tests/test_landing_page.py index.html
git commit -m "feat: add trust-focused testimonials FAQ and process details"
```

## Task 4: CTA 일관성/추적 스크립트/반응형 품질 추가

**Files:**
- Modify: `tests/test_landing_page.py`
- Modify: `index.html`
- Test: `tests/test_landing_page.py`

- [ ] **Step 1: 실패 테스트 추가 (CTA 통일/추적/모바일 메타 검증)**

```python
import re

    def test_all_cta_use_same_kakao_link_token(self):
        html = self.read_html()
        hrefs = re.findall(r'class="js-kakao-cta"\s+href="([^"]+)"', html)
        self.assertGreaterEqual(len(hrefs), 3)
        self.assertEqual(len(set(hrefs)), 1)
        self.assertEqual(hrefs[0], "__KAKAO_CHAT_URL__")

    def test_tracking_script_and_viewport_exist(self):
        html = self.read_html()
        self.assertIn('name="viewport"', html)
        self.assertIn("function trackConsultClick", html)
        self.assertIn("js-kakao-cta", html)
```

- [ ] **Step 2: 테스트 실행하여 실패 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: FAIL (CTA 개수 부족 또는 추적 함수 미존재)

- [ ] **Step 3: 최소 구현 작성 (CTA 추가, 스타일, 추적 코드 반영)**

```html
<style>
  :root {
    color-scheme: light;
  }
  body {
    margin: 0;
    font-family: "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
    color: #1f2937;
    background: #f8fafc;
    line-height: 1.6;
  }
  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 24px 16px 88px;
  }
  .card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 16px;
  }
  .cta {
    display: inline-block;
    background: #0f766e;
    color: #ffffff;
    text-decoration: none;
    border-radius: 10px;
    padding: 12px 18px;
    font-weight: 700;
  }
  .cta-fixed {
    position: fixed;
    left: 16px;
    right: 16px;
    bottom: 16px;
    text-align: center;
  }
  .cta-fixed .cta {
    width: 100%;
    min-height: 48px;
    line-height: 24px;
    padding-top: 12px;
    padding-bottom: 12px;
  }
</style>

<div class="container">
  <section id="hero" class="card">
    <h1>40대 이상 성인을 위한 AI 코드 어시스턴스 교육</h1>
    <p>복잡한 설명 대신, 바로 활용 가능한 학습을 제공합니다.</p>
    <a class="cta js-kakao-cta" href="__KAKAO_CHAT_URL__">카카오톡 상담 신청</a>
  </section>

  <section id="curriculum" class="card">...</section>
  <section id="testimonials" class="card">...</section>
  <section id="process" class="card">
    <p>상담 신청 → 학습 진단 → 수강 진행 → 상담 후 계좌이체</p>
    <a class="cta js-kakao-cta" href="__KAKAO_CHAT_URL__">진행 방식 상담하기</a>
  </section>
  <section id="faq" class="card">...</section>
  <section id="final-cta" class="card">
    <a class="cta js-kakao-cta" href="__KAKAO_CHAT_URL__">지금 상담 신청하기</a>
  </section>
</div>

<div class="cta-fixed">
  <a class="cta js-kakao-cta" href="__KAKAO_CHAT_URL__">카카오톡으로 바로 상담</a>
</div>

<script>
  function trackConsultClick(position) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "consult_click",
      position,
      timestamp: Date.now(),
    });
  }

  document.querySelectorAll(".js-kakao-cta").forEach((button, index) => {
    button.addEventListener("click", () => {
      trackConsultClick(`cta_${index + 1}`);
    });
  });
</script>
```

- [ ] **Step 4: 테스트 재실행하여 통과 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: PASS (7 tests)

- [ ] **Step 5: 커밋**

```bash
git add tests/test_landing_page.py index.html
git commit -m "feat: unify kakao CTA links and add click tracking"
```

## Task 5: 오픈 전 검증 루틴 고정

**Files:**
- Modify: `tests/test_landing_page.py`
- Modify: `index.html`
- Test: `tests/test_landing_page.py`

- [ ] **Step 1: 실패 테스트 추가 (런치 체크 문구 검증)**

```python
    def test_launch_checklist_copy_exists(self):
        html = self.read_html()
        self.assertIn("카카오 링크", html)
        self.assertIn("모바일", html)
        self.assertIn("FAQ", html)
```

- [ ] **Step 2: 테스트 실행하여 실패 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: FAIL (`AssertionError` for missing launch checklist copy)

- [ ] **Step 3: 최소 구현 작성 (페이지 하단에 검증 체크리스트 추가)**

```html
<section id="launch-checklist" class="card">
  <h2>오픈 전 점검</h2>
  <ul>
    <li>카카오 링크 최종 반영 여부 확인</li>
    <li>상/중/하 CTA 동작 확인</li>
    <li>모바일 가독성과 버튼 터치 영역 확인</li>
    <li>FAQ 핵심 항목 최신화 확인</li>
  </ul>
</section>
```

- [ ] **Step 4: 전체 테스트 실행 및 수동 확인**

Run: `python -m unittest tests/test_landing_page.py -v`  
Expected: PASS (8 tests)

Run: `python -m http.server 8000`  
Expected: `Serving HTTP on` 출력 후 브라우저에서 `http://localhost:8000/index.html` 접속 가능

수동 확인:
- 상담 CTA 4개 이상 노출 여부
- 모든 CTA가 동일 링크(`__KAKAO_CHAT_URL__`)인지 요소 검사로 확인
- 390px 폭 모바일 뷰에서 하단 CTA가 화면 밖으로 잘리지 않는지 확인

- [ ] **Step 5: 커밋**

```bash
git add tests/test_landing_page.py index.html
git commit -m "chore: add launch checklist content and final verification"
```

## Self-Review 결과

1. **Spec coverage:**
- 목표/KPI(주간 상담 신청 건수): Task 2
- 타깃(40대 이상 성인): Task 2
- A안 단일 롱스크롤 구조: Task 1
- 핵심 섹션 6개: Task 1~3
- 후기/사례 강조: Task 3
- 상담 후 계좌이체 흐름: Task 1, Task 3
- CTA 카카오톡 통일: Task 4
- 모바일/품질 점검: Task 4, Task 5

2. **Placeholder scan:**
- `TODO`, `TBD`, "적절히" 같은 모호 지시 없음
- 모든 코드 변경 단계에 코드 블록 포함됨

3. **Type consistency:**
- CTA 클래스 `.js-kakao-cta` 일관 사용
- 추적 함수명 `trackConsultClick` 일관 사용
- 테스트 파일 경로/명령 일관 사용
