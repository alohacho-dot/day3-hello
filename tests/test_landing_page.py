import re
import unittest
from pathlib import Path


class LandingPageTest(unittest.TestCase):
    def read_html(self) -> str:
        project_root = Path(__file__).resolve().parent.parent
        return (project_root / "index.html").read_text(encoding="utf-8")

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
            self.assertRegex(html, rf"id\s*=\s*['\"]{section_id}['\"]")
    def test_consultation_and_payment_flow_text_exists(self):
        html = self.read_html()
        self.assertIn("상담 신청", html)
        self.assertIn("상담 후 계좌이체", html)

    def test_target_and_curriculum_copy_exists(self):
        html = self.read_html()
        self.assertIn("40대 이상 성인", html)
        self.assertIn("초급", html)
        self.assertIn("활용", html)
        self.assertIn("실전", html)
        self.assertIn("주간 상담 신청 건수", html)

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

    def test_all_js_kakao_cta_use_same_kakao_link_token(self):
        html = self.read_html()
        hrefs = re.findall(
            r'<a[^>]*class=["\'][^"\']*js-kakao-cta[^"\']*["\'][^>]*href=["\']([^"\']+)["\']',
            html,
        )
        self.assertGreaterEqual(len(hrefs), 3)
        self.assertEqual(len(set(hrefs)), 1)
        self.assertEqual(hrefs[0], "__KAKAO_CHAT_URL__")

    def test_viewport_meta_exists(self):
        html = self.read_html()
        self.assertRegex(
            html,
            r'<meta[^>]*name=["\']viewport["\'][^>]*>',
        )

    def test_track_consult_click_function_exists(self):
        html = self.read_html()
        self.assertIn("function trackConsultClick", html)

    def test_launch_checklist_copy_exists(self):
        html = self.read_html()
        self.assertIn("카카오 링크", html)
        self.assertIn("모바일", html)
        self.assertIn("FAQ", html)


if __name__ == "__main__":
    unittest.main()
