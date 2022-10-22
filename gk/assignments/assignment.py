import gk.assignments.api as api

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def check_assignment(step_num: int, test_num: int, name: str, answers: dict):
    eprint('\n--------- #%s. Checking assignment: %s' % (test_num, name))
    gk_api = api.GkApi()

    req = api.GkAssignmentRequest(step_num, test_num, answers)
    is_ok = False

    try:
        resp = gk_api.do_assignments(req)
        if resp['is_ok']:
            eprint('OK!')
            is_ok = True
        else:
            eprint('FAILED!')
            eprint('\tKey<%s>: expected<%s> but got<%s>' % (resp['key'], resp['expected'], resp['got']))
    except Exception as e:
        eprint(f'Error: %s' % e)

    eprint('--------- #%s. End\n' % test_num)
    return is_ok


if __name__ == '__main__':
    import os
    os.chdir('../..')
    check_assignment(5, 1, 'should calculate rent', {"a": "a", "b": "b"})
