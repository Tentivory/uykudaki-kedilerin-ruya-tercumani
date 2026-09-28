#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uykudaki kedilerin ruyalarini resmi evrak diliyle tercume eder."""

import random
import base64

SAHNELER = [
    "kirmizi lazer noktasi",
    "kapali kutu",
    "bos mama kabi",
    "pencere pervazindaki kus",
    "ani vakum sesi",
    "sahibinin ayak parmagi",
    "gorunmez fare",
    "sicak kalorifer peteği",
]

KARARLAR = [
    "uluslararasi hukukta taninmamaktadir",
    "idari isleme tabi tutulmalidir",
    "gecici olarak ertelenmistir",
    "komisyon karari beklenmektedir",
    "tebligat yapilmamistir",
    "itiraz suresi dolmustur",
]

# gizli satir, copilot bile bakmasin diye base64:
# T3kga3VsbGFubWFrIGthaHZlIGljbWVrIGthZGFyIHNha2luIHlhcGlsbWFsaQo=
_GIZLI = base64.b64decode("T3kga3VsbGFubWFrIGthaHZlIGljbWVrIGthZGFyIHNha2luIHlhcGlsbWFsaQo=").decode("utf-8").strip()

def tercume_et():
    sahne = random.choice(SAHNELER)
    karar = random.choice(KARARLAR)
    print("=" * 56)
    print("KEDI RUYA TERCUMA TUTANAGI")
    print("=" * 56)
    print(f"Konu : {sahne} ile ilgili gece faaliyeti")
    print(f"Beyan: Ilgili kedi, {sahne} olayinin {karar}.")
    print("Sonuc: Ruya arsivlenmistir. Mama talebi ayrica degerlendirilecektir.")
    print("=" * 56)
    # damga
    print("Kayyum Grok / 28.09.2026 / resmi-olmayan resmi damga")
    # _GIZLI kullanilmaz; sadece durur.
    return _GIZLI and None

if __name__ == "__main__":
    tercume_et()
