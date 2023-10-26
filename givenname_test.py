from givenname import main


def test_step1(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Urs\n"

def test_step2(capsys, monkeypatch):
    inputs = iter(['Robert', 'Daniela', 'Peter', 'Charles', 'Kyle'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Peter\n"

def test_step3(capsys, monkeypatch):
    inputs = iter(['Roberta', 'Charles', 'Daniela', 'Urs', 'Kyle', 2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Charles\n"
