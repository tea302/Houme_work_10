import json



def load_candidates() -> list[dict]:

    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
              {candidate["name"]}\n
              {candidate["position"]}\n
              {candidate["skills"]}\n
          """
    result += '</pre>'

def get_all_candidates() -> list[dict]:
    return load_candidates()

def get_candidate_by_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidate_by_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


# `load_candidates()`, которая загрузит данные из файла
#
# `get_all()`, которая покажет всех кандидатов
#
# `get_by_pk(pk)`, которая вернет кандидата по pk
#
# `get_by_skill(skill_name)`, которая вернет кандидатов по навыку