from fastapi import APIRouter

from examples import (
    boolean_operators,
    dictionaries,
    for_while,
    functional,
    lists,
    oop,
    operators,
    sets,
    strings,
    type_hints,
    types,
)

router = APIRouter(prefix="/examples", tags=["Examples"])


@router.get("/boolean-operators")
async def get_boolean_operators():
    boolean_operators.main()


@router.get("/for-while")
async def get_for_while():
    for_while.main()


@router.get("/lists")
async def get_lists():
    lists.main()


@router.get("/dictionaries")
async def get_dictionaries():
    dictionaries.main()


@router.get("/functional")
async def get_functional():
    functional.main()


@router.get("/oop")
async def get_oop():
    oop.main()


@router.get("/operators")
async def get_operators():
    operators.main()


@router.get("/sets")
async def get_sets():
    sets.main()


@router.get("/type-hints")
async def get_type_hints():
    type_hints.main()


@router.get("/types")
async def get_types():
    types.main()


@router.get("/strings")
async def get_strings():
    strings.main()
