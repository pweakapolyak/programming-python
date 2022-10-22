import api

gk_api = api.GkApi()


def check_assignment(step_num: int, test_num: int, name: str, answers: dict):
    print('\n--------- #%s. Checking assignment: %s' % (test_num, name))

    req = api.GkAssignmentRequest(step_num, test_num, answers)
    try:
        resp = gk_api.do_assignments(req)
        if resp['is_ok']:
            print('OK!')
        else:
            print('FAILED!')
            print('\tKey<%s>: expected<%s> but got<%s>' % (resp['key.txt'], resp['expected'], resp['got']))
    except Exception as e:
        print(f'Error: %s' % e)

    print('--------- #%s. End\n' % test_num)


if __name__ == '__main__':
    check_assignment(5, 1, 'should calculate rent', {"a": "a", "b": "b"})
