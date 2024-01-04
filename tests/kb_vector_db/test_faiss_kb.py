from pprint import pprint

from server.knowledge_base.kb_service.faiss_kb_service import FaissKBService
from server.knowledge_base.migrate import create_tables
from server.knowledge_base.utils import KnowledgeFile


kbService = FaissKBService("okcard")
test_kb_name = "okcard"
test_file_name = "ok卡帮助中心.xlsx"
testKnowledgeFile = KnowledgeFile(test_file_name, test_kb_name)
search_content = "怎么买卡"


def test_init():
    create_tables()


def test_create_db():
    assert kbService.create_kb()


def test_add_doc():
    assert kbService.add_doc(testKnowledgeFile)


def test_search_db():
    print('\n')
    result = kbService.search_docs(search_content)
    pprint(result)
    assert len(result) > 0


def test_delete_doc():
    assert kbService.delete_doc(testKnowledgeFile)


def test_delete_db():
    assert kbService.drop_kb()
