from givenname import main


def test_step1(capsys, monkeypatch):
    inputs = iter(['Robert', 'Daniela', 'Urs', 'Charles', 'Kyle', 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Urs\n"


def test_step2(capsys, monkeypatch):
    inputs = iter(['Robert', 'Daniela', 'Urs', 'Charles', 'Kyle', 3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Urs\n"


def test_step3(capsys, monkeypatch):
    inputs = iter(['Roberta', 'Urs', 'Daniela', 'Charles', 'Kyle', 2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Urs\n"
