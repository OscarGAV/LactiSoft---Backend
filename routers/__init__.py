from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_current_user
from models import (
    Departamento, Provincia, Distrito, Direccion, Usuario,
    Telefono, Conductor, Inspector, Transporte, RolEmpresa,
    TipoCanal, Empresa, Canal, Consumidor, Flota, PuntoVenta,
    CentroAcopio, ReporteCalidad, Producto, DetalleProducto,
    OrdenTransporte, CabeceraFactura, MedioPago, Factura,
)
from schemas import (
    DepartamentoCreate, DepartamentoUpdate, DepartamentoOut,
    ProvinciaCreate, ProvinciaUpdate, ProvinciaOut,
    DistritoCreate, DistritoUpdate, DistritoOut,
    DireccionCreate, DireccionUpdate, DireccionOut,
    UsuarioOut, UsuarioUpdate,
    TelefonoCreate, TelefonoUpdate, TelefonoOut,
    ConductorCreate, ConductorUpdate, ConductorOut,
    InspectorCreate, InspectorUpdate, InspectorOut,
    TransporteCreate, TransporteUpdate, TransporteOut,
    RolEmpresaCreate, RolEmpresaUpdate, RolEmpresaOut,
    TipoCanalCreate, TipoCanalUpdate, TipoCanalOut,
    EmpresaCreate, EmpresaUpdate, EmpresaOut,
    CanalCreate, CanalUpdate, CanalOut,
    ConsumidorCreate, ConsumidorUpdate, ConsumidorOut,
    FlotaCreate, FlotaUpdate, FlotaOut,
    PuntoVentaCreate, PuntoVentaUpdate, PuntoVentaOut,
    CentroAcopioCreate, CentroAcopioUpdate, CentroAcopioOut,
    ReporteCalidadCreate, ReporteCalidadUpdate, ReporteCalidadOut,
    ProductoCreate, ProductoUpdate, ProductoOut,
    DetalleProductoCreate, DetalleProductoUpdate, DetalleProductoOut,
    OrdenTransporteCreate, OrdenTransporteUpdate, OrdenTransporteOut,
    CabeceraFacturaCreate, CabeceraFacturaUpdate, CabeceraFacturaOut,
    MedioPagoCreate, MedioPagoUpdate, MedioPagoOut,
    FacturaCreate, FacturaUpdate, FacturaOut,
)
from services import CRUDBase

_auth = Depends(get_current_user)


def _router(prefix: str, tag: str, crud, Out, Create, Update, pk_type=int):
    r = APIRouter(prefix=prefix, tags=[tag])

    @r.get("/", response_model=list[Out])
    def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=_auth):
        return crud.get_all(db, skip, limit)

    @r.get("/{pk}", response_model=Out)
    def get_one(pk: pk_type, db: Session = Depends(get_db), _=_auth):
        return crud.get(db, pk)

    @r.post("/", response_model=Out, status_code=201)
    def create(body: Create, db: Session = Depends(get_db), _=_auth):
        return crud.create(db, body)

    @r.patch("/{pk}", response_model=Out)
    def update(pk: pk_type, body: Update, db: Session = Depends(get_db), _=_auth):
        return crud.update(db, pk, body)

    @r.delete("/{pk}")
    def delete(pk: pk_type, db: Session = Depends(get_db), _=_auth):
        return crud.delete(db, pk)

    return r


departamentos_router = _router(
    "/departamentos", "Departamentos",
    CRUDBase(Departamento), DepartamentoOut, DepartamentoCreate, DepartamentoUpdate,
)
provincias_router = _router(
    "/provincias", "Provincias",
    CRUDBase(Provincia), ProvinciaOut, ProvinciaCreate, ProvinciaUpdate,
)
distritos_router = _router(
    "/distritos", "Distritos",
    CRUDBase(Distrito), DistritoOut, DistritoCreate, DistritoUpdate,
)
direcciones_router = _router(
    "/direcciones", "Direcciones",
    CRUDBase(Direccion), DireccionOut, DireccionCreate, DireccionUpdate,
)
usuarios_router = _router(
    "/usuarios", "Usuarios",
    CRUDBase(Usuario), UsuarioOut, UsuarioOut, UsuarioUpdate,
)
telefonos_router = _router(
    "/telefonos", "Telefonos",
    CRUDBase(Telefono), TelefonoOut, TelefonoCreate, TelefonoUpdate,
)
conductores_router = _router(
    "/conductores", "Conductores",
    CRUDBase(Conductor), ConductorOut, ConductorCreate, ConductorUpdate,
)
inspectores_router = _router(
    "/inspectores", "Inspectores",
    CRUDBase(Inspector), InspectorOut, InspectorCreate, InspectorUpdate,
)
transportes_router = _router(
    "/transportes", "Transportes",
    CRUDBase(Transporte), TransporteOut, TransporteCreate, TransporteUpdate,
)
roles_empresa_router = _router(
    "/roles-empresa", "Roles de Empresas",
    CRUDBase(RolEmpresa), RolEmpresaOut, RolEmpresaCreate, RolEmpresaUpdate,
)
tipos_canal_router = _router(
    "/tipos-canal", "Tipos de Canales",
    CRUDBase(TipoCanal), TipoCanalOut, TipoCanalCreate, TipoCanalUpdate,
)
empresas_router = _router(
    "/empresas", "Empresas",
    CRUDBase(Empresa), EmpresaOut, EmpresaCreate, EmpresaUpdate,
)
canales_router = _router(
    "/canales", "Canales",
    CRUDBase(Canal), CanalOut, CanalCreate, CanalUpdate,
)
consumidores_router = _router(
    "/consumidores", "Consumidores",
    CRUDBase(Consumidor), ConsumidorOut, ConsumidorCreate, ConsumidorUpdate,
)
flotas_router = _router(
    "/flotas", "Flotas",
    CRUDBase(Flota), FlotaOut, FlotaCreate, FlotaUpdate,
)
puntos_venta_router = _router(
    "/puntos-venta", "Puntos de Venta",
    CRUDBase(PuntoVenta), PuntoVentaOut, PuntoVentaCreate, PuntoVentaUpdate,
)
centros_acopio_router = _router(
    "/centros-acopio", "Centros de Acopio",
    CRUDBase(CentroAcopio), CentroAcopioOut, CentroAcopioCreate, CentroAcopioUpdate,
)
reportes_calidad_router = _router(
    "/reportes-calidad", "Reportes de Calidad",
    CRUDBase(ReporteCalidad), ReporteCalidadOut, ReporteCalidadCreate, ReporteCalidadUpdate,
)
productos_router = _router(
    "/productos", "Productos",
    CRUDBase(Producto), ProductoOut, ProductoCreate, ProductoUpdate,
)
detalles_producto_router = _router(
    "/detalles-producto", "Detalles de Productos",
    CRUDBase(DetalleProducto), DetalleProductoOut, DetalleProductoCreate, DetalleProductoUpdate,
)
ordenes_router = _router(
    "/ordenes", "Ordenes de Transporte",
    CRUDBase(OrdenTransporte), OrdenTransporteOut, OrdenTransporteCreate, OrdenTransporteUpdate,
)
cabeceras_factura_router = _router(
    "/cabeceras-factura", "Cabeceras de Facturas",
    CRUDBase(CabeceraFactura), CabeceraFacturaOut, CabeceraFacturaCreate, CabeceraFacturaUpdate,
)
medios_pago_router = _router(
    "/medios-pago", "Medios de Pago",
    CRUDBase(MedioPago), MedioPagoOut, MedioPagoCreate, MedioPagoUpdate,
)
facturas_router = _router(
    "/facturas", "Facturas",
    CRUDBase(Factura), FacturaOut, FacturaCreate, FacturaUpdate,
)
