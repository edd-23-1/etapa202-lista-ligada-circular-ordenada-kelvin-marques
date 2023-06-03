# ATENÇÃO: Não altere o código de arquivo
import os.path
import sys
from pytest import mark, raises
from no import No
from lista_ligada_circular_ordenada import ListaLigadaCircularOrdenada


# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    result = lista_circular.is_empty()
    expected = True

    assert result == expected and lista_circular.size() == 0


def test_is_empty_false():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(3)
    lista_circular.add(1)
    lista_circular.add(2)

    result = lista_circular.is_empty()
    expected = False

    assert result == expected and lista_circular.size() == 2

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(1)
    lista_circular.add(1)

    result = lista_circular.is_full()
    expected = True

    assert result == expected and lista_circular.size() == 1


def test_is_full_false():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(3)
    lista_circular.add(1)
    lista_circular.add(2)

    result = lista_circular.is_full()
    expected = False

    assert result == expected and lista_circular.size() == 2

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método add()

def test_add_em_lista_circular_cheia():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(1)

    lista_circular.add(1)

    result = lista_circular.contains(1)
    expected = True

    assert result == expected
    with raises(Exception):
        lista_circular.add(2) # deve gerar erro


def test_add_em_lista_circular_vazia():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    result = lista_circular.add(1)
    result = lista_circular.add(2)
    expected = True

    assert result == expected and lista_circular.size() == 2


def test_add_em_lista_circular_para_verificar_ordem_aleatoria():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(10)

    lista_circular.add(1)
    lista_circular.add(4)
    lista_circular.add(2)
    lista_circular.add(3)
    lista_circular.add(5)

    result = lista_circular.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_circular_para_verificar_ordem_crescente():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(10)

    lista_circular.add(1)
    lista_circular.add(2)
    lista_circular.add(3)
    lista_circular.add(4)
    lista_circular.add(5)

    result = lista_circular.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_circular_para_verificar_ordem_decrescente():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada(10)

    lista_circular.add(5)
    lista_circular.add(4)
    lista_circular.add(3)
    lista_circular.add(2)
    lista_circular.add(1)

    result = lista_circular.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected

# ---- FIM: teste método add()


# ---- INÍCIO: teste método remove()

def test_remove_em_lista_circular_vazia():

    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with raises(Exception):
        lista_circular.remove() # deve gerar erro


def test_remove_em_lista_circular_com_item_presente_no_meio():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    result = lista_circular.remove('3')
    expected = True

    assert expected == result

    result = lista_circular.display()
    expected = [
        '1',
        '2',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_circular_com_item_presente_no_inicio():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    result = lista_circular.remove('1')
    expected = True

    assert expected == result

    result = lista_circular.display()
    expected = [
        '2',
        '3',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_circular_com_item_presente_no_fim():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    result = lista_circular.remove('5')
    expected = True

    assert expected == result

    result = lista_circular.display()
    expected = [
        '1',
        '2',
        '3',
        '4'
    ]

    assert expected == result


def test_remove_em_lista_circular_sem_item_presente():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    result = lista_circular.remove('9')
    expected = False

    assert expected == result


def test_remove_em_lista_circular_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    for x in range(5):
      lista_circular.remove(str(x+1))

    with raises(Exception):
        lista_circular.remove(1) # deve gerar erro

# ---- FIM: teste método remove()


# ---- INÍCIO: teste método contains()

def test_contains_em_lista_circular_vazia():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    result = lista_circular.contains(1)
    expected = False

    assert expected == result


def test_contains_em_lista_circular_com_item_presente():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()
    lista_circular.add(1)

    result = lista_circular.contains(1)
    expected = True

    assert expected == result


def test_contains_em_lista_circular_sem_item_presente():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()
    lista_circular.add(1)

    result = lista_circular.contains(2)
    expected = False

    assert expected == result

# ---- FIM: teste método contains()


# ---- INÍCIO: teste método display()

def test_display_em_lista_circular_com_elementos_string():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_circular.add(item[:-1])

    result = lista_circular.display()
    expected = [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

    assert result == expected


def test_display_em_lista_circular_com_elementos_int():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    lista_circular.add(1)
    lista_circular.add(2)
    lista_circular.add(3)

    result = lista_circular.display()
    expected = [
        1,
        2,
        3,
    ]

    assert result == expected


def test_display_em_lista_circular_sem_elementos_ao_criar_lista_circular():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    result = lista_circular.display()
    expected = []
    
    assert result == expected


def test_display_em_lista_circular_sem_elementos_ao_esvaziar_lista_circular():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    lista_circular.add(1)
    lista_circular.add(2)
    lista_circular.remove(2)
    lista_circular.remove(1)

    result = lista_circular.display()
    expected = []
    
    assert result == expected

# ---- FIM: teste método display()


# ---- INÍCIO: teste método size()

def test_size_em_lista_circular_ao_criar_lista():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    result = lista_circular.size()
    expected = 0
    
    assert result == expected


def test_size_em_lista_circular_ao_inserir_itens():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    lista_circular.add(1)
    expected = 1
    assert lista_circular.size() == expected

    lista_circular.add(1)
    expected = 2
    assert lista_circular.size() == expected

    lista_circular.add(1)
    expected = 3
    assert lista_circular.size() == expected


def test_size_ao_remover_itens():
    try:
        exists = os.path.exists("lista_ligada_circular_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_circular = ListaLigadaCircularOrdenada()

    lista_circular.add(1)
    lista_circular.add(1)
    lista_circular.add(1)

    lista_circular.remove(1)
    result = lista_circular.size()
    expected = 2
    assert result == expected

    lista_circular.remove(1)
    result = lista_circular.size()
    expected = 1
    assert result == expected

    lista_circular.remove(1)
    result = lista_circular.size()
    expected = 0
    assert result == expected

# ---- FIM: teste método size()