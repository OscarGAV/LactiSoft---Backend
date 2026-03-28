from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, field_validator


# ── Auth ───────────────────────────────────────────────────
class LoginRequest(BaseModel):
    Usuario_DNI: str
    Usuario_Password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Departamento ───────────────────────────────────────────
class DepartamentoBase(BaseModel):
    Dpto_Nombre: str

class DepartamentoCreate(DepartamentoBase): pass

class DepartamentoUpdate(BaseModel):
    Dpto_Nombre: Optional[str] = None

class DepartamentoOut(DepartamentoBase):
    Dpto_ID: int
    model_config = {"from_attributes": True}


# ── Provincia ──────────────────────────────────────────────
class ProvinciaBase(BaseModel):
    Prov_Nombre: str
    Prov_Dpto_ID: int

class ProvinciaCreate(ProvinciaBase): pass

class ProvinciaUpdate(BaseModel):
    Prov_Nombre: Optional[str] = None
    Prov_Dpto_ID: Optional[int] = None

class ProvinciaOut(ProvinciaBase):
    Prov_ID: int
    model_config = {"from_attributes": True}


# ── Distrito ───────────────────────────────────────────────
class DistritoBase(BaseModel):
    Distrito_Nombre: str
    Distrito_Prov_ID: int

class DistritoCreate(DistritoBase): pass

class DistritoUpdate(BaseModel):
    Distrito_Nombre: Optional[str] = None
    Distrito_Prov_ID: Optional[int] = None

class DistritoOut(DistritoBase):
    Distrito_ID: int
    model_config = {"from_attributes": True}


# ── Direccion ──────────────────────────────────────────────
class DireccionBase(BaseModel):
    Direccion_Nombre: str
    Direccion_Latitud: Optional[Decimal] = None
    Direccion_Altitud: Optional[Decimal] = None
    Direccion_Distrito_ID: int

class DireccionCreate(DireccionBase): pass

class DireccionUpdate(BaseModel):
    Direccion_Nombre: Optional[str] = None
    Direccion_Latitud: Optional[Decimal] = None
    Direccion_Altitud: Optional[Decimal] = None
    Direccion_Distrito_ID: Optional[int] = None

class DireccionOut(DireccionBase):
    Direccion_ID: int
    model_config = {"from_attributes": True}


# ── Usuario ────────────────────────────────────────────────
class UsuarioRegister(BaseModel):
    Usuario_Nombres: str
    Usuario_Apellidos: str
    Usuario_FechaNacimiento: Optional[date] = None
    Usuario_DNI: str
    Usuario_Rol: str
    Usuario_Password: str

    @field_validator("Usuario_DNI")
    @classmethod
    def dni_length(cls, v: str) -> str:
        if len(v) != 8:
            raise ValueError("El DNI debe tener exactamente 8 caracteres")
        return v

    @field_validator("Usuario_Rol")
    @classmethod
    def rol_valid(cls, v: str) -> str:
        if v not in ("A", "C", "I", "T", "V"):
            raise ValueError("Rol invalido. Valores permitidos: A, C, I, T, V")
        return v

class UsuarioUpdate(BaseModel):
    Usuario_Nombres: Optional[str] = None
    Usuario_Apellidos: Optional[str] = None
    Usuario_FechaNacimiento: Optional[date] = None
    Usuario_Rol: Optional[str] = None
    Usuario_Password: Optional[str] = None

class UsuarioOut(BaseModel):
    Usuario_ID: int
    Usuario_Nombres: str
    Usuario_Apellidos: str
    Usuario_FechaNacimiento: Optional[date] = None
    Usuario_DNI: str
    Usuario_Rol: str
    model_config = {"from_attributes": True}


# ── Telefono ───────────────────────────────────────────────
class TelefonoBase(BaseModel):
    Telefono_Nro: str
    Telefono_Prefijo: Optional[str] = None
    Telefono_Usuario_ID: int

class TelefonoCreate(TelefonoBase): pass

class TelefonoUpdate(BaseModel):
    Telefono_Nro: Optional[str] = None
    Telefono_Prefijo: Optional[str] = None

class TelefonoOut(TelefonoBase):
    Telefono_ID: int
    model_config = {"from_attributes": True}


# ── Conductor ──────────────────────────────────────────────
class ConductorBase(BaseModel):
    Conductor_Licencia: bool = False
    Conductor_Antecedentes: bool = False
    Conductor_SeguroVehicular: bool = False
    Conductor_Usuario_ID: int

class ConductorCreate(ConductorBase): pass

class ConductorUpdate(BaseModel):
    Conductor_Licencia: Optional[bool] = None
    Conductor_Antecedentes: Optional[bool] = None
    Conductor_SeguroVehicular: Optional[bool] = None

class ConductorOut(ConductorBase):
    Conductor_ID: int
    model_config = {"from_attributes": True}


# ── Inspector ──────────────────────────────────────────────
class InspectorBase(BaseModel):
    Inspector_Usuario_ID: int

class InspectorCreate(InspectorBase): pass

class InspectorUpdate(BaseModel):
    Inspector_Usuario_ID: Optional[int] = None

class InspectorOut(InspectorBase):
    Inspector_ID: int
    model_config = {"from_attributes": True}


# ── Transporte ─────────────────────────────────────────────
class TransporteBase(BaseModel):
    Transporte_NroPlaca: str
    Transporte_Conductor_ID: int

class TransporteCreate(TransporteBase): pass

class TransporteUpdate(BaseModel):
    Transporte_NroPlaca: Optional[str] = None
    Transporte_Conductor_ID: Optional[int] = None

class TransporteOut(TransporteBase):
    Transporte_ID: int
    model_config = {"from_attributes": True}


# ── RolEmpresa ─────────────────────────────────────────────
class RolEmpresaBase(BaseModel):
    EmpresaRol_Tipo: str

class RolEmpresaCreate(RolEmpresaBase): pass

class RolEmpresaUpdate(BaseModel):
    EmpresaRol_Tipo: Optional[str] = None

class RolEmpresaOut(RolEmpresaBase):
    EmpresaRol_ID: int
    model_config = {"from_attributes": True}


# ── TipoCanal ──────────────────────────────────────────────
class TipoCanalBase(BaseModel):
    TipoCanal_Nombre: str

class TipoCanalCreate(TipoCanalBase): pass

class TipoCanalUpdate(BaseModel):
    TipoCanal_Nombre: Optional[str] = None

class TipoCanalOut(TipoCanalBase):
    TipoCanal_ID: int
    model_config = {"from_attributes": True}


# ── Empresa ────────────────────────────────────────────────
class EmpresaBase(BaseModel):
    Empresa_Nombre: str
    Empresa_RazonSocial: Optional[str] = None
    Empresa_Rol_ID: int

class EmpresaCreate(EmpresaBase): pass

class EmpresaUpdate(BaseModel):
    Empresa_Nombre: Optional[str] = None
    Empresa_RazonSocial: Optional[str] = None
    Empresa_Rol_ID: Optional[int] = None

class EmpresaOut(EmpresaBase):
    Empresa_ID: int
    model_config = {"from_attributes": True}


# ── Canal ──────────────────────────────────────────────────
class CanalBase(BaseModel):
    Canal_Enlace: str
    Canal_TipoCanal_ID: int
    Canal_Empresa_ID: int

class CanalCreate(CanalBase): pass

class CanalUpdate(BaseModel):
    Canal_Enlace: Optional[str] = None
    Canal_TipoCanal_ID: Optional[int] = None
    Canal_Empresa_ID: Optional[int] = None

class CanalOut(CanalBase):
    Canal_ID: int
    model_config = {"from_attributes": True}


# ── Consumidor ─────────────────────────────────────────────
class ConsumidorBase(BaseModel):
    Consumidor_Direccion_ID: int
    Consumidor_Usuario_ID: int

class ConsumidorCreate(ConsumidorBase): pass

class ConsumidorUpdate(BaseModel):
    Consumidor_Direccion_ID: Optional[int] = None

class ConsumidorOut(ConsumidorBase):
    Consumidor_ID: int
    model_config = {"from_attributes": True}


# ── Flota ──────────────────────────────────────────────────
class FlotaBase(BaseModel):
    Flota_Distrito_ID: int
    Flota_Transporte_ID: int

class FlotaCreate(FlotaBase): pass

class FlotaUpdate(BaseModel):
    Flota_Distrito_ID: Optional[int] = None
    Flota_Transporte_ID: Optional[int] = None

class FlotaOut(FlotaBase):
    Flota_ID: int
    model_config = {"from_attributes": True}


# ── PuntoVenta ─────────────────────────────────────────────
class PuntoVentaBase(BaseModel):
    PuntoVenta_Nombre: str
    PuntoVenta_Direccion_ID: int
    PuntoVenta_Flota_ID: int

class PuntoVentaCreate(PuntoVentaBase): pass

class PuntoVentaUpdate(BaseModel):
    PuntoVenta_Nombre: Optional[str] = None
    PuntoVenta_Direccion_ID: Optional[int] = None
    PuntoVenta_Flota_ID: Optional[int] = None

class PuntoVentaOut(PuntoVentaBase):
    PuntoVenta_ID: int
    model_config = {"from_attributes": True}


# ── CentroAcopio ───────────────────────────────────────────
class CentroAcopioBase(BaseModel):
    CentroAcopio_Nombre: str
    CentroAcopio_CapacidadTotal: Optional[int] = None
    CentroAcopio_Direccion_ID: int

class CentroAcopioCreate(CentroAcopioBase): pass

class CentroAcopioUpdate(BaseModel):
    CentroAcopio_Nombre: Optional[str] = None
    CentroAcopio_CapacidadTotal: Optional[int] = None
    CentroAcopio_Direccion_ID: Optional[int] = None

class CentroAcopioOut(CentroAcopioBase):
    CentroAcopio_ID: int
    model_config = {"from_attributes": True}


# ── ReporteCalidad ─────────────────────────────────────────
class ReporteCalidadBase(BaseModel):
    ReporteCalidad_Fecha: Optional[date] = None
    ReporteCalidad_Inspector_ID: int

class ReporteCalidadCreate(ReporteCalidadBase): pass

class ReporteCalidadUpdate(BaseModel):
    ReporteCalidad_Fecha: Optional[date] = None
    ReporteCalidad_Inspector_ID: Optional[int] = None

class ReporteCalidadOut(ReporteCalidadBase):
    ReporteCalidad_ID: int
    model_config = {"from_attributes": True}


# ── Producto ───────────────────────────────────────────────
class ProductoBase(BaseModel):
    Producto_Nombre: str
    Producto_Codigo: str
    Producto_Empresa_ID: int
    Producto_ReporteCalidad_ID: Optional[int] = None
    Producto_CentroAcopio_ID: int

class ProductoCreate(ProductoBase): pass

class ProductoUpdate(BaseModel):
    Producto_Nombre: Optional[str] = None
    Producto_Codigo: Optional[str] = None
    Producto_Empresa_ID: Optional[int] = None
    Producto_ReporteCalidad_ID: Optional[int] = None
    Producto_CentroAcopio_ID: Optional[int] = None

class ProductoOut(ProductoBase):
    Producto_ID: int
    model_config = {"from_attributes": True}


# ── DetalleProducto ────────────────────────────────────────
class DetalleProductoBase(BaseModel):
    DetalleProducto_FechaVencimiento: Optional[date] = None
    DetalleProducto_PrecioUnitario: Optional[Decimal] = None
    DetalleProducto_Stock: Optional[int] = None
    DetalleProducto_Producto_ID: int

class DetalleProductoCreate(DetalleProductoBase): pass

class DetalleProductoUpdate(BaseModel):
    DetalleProducto_FechaVencimiento: Optional[date] = None
    DetalleProducto_PrecioUnitario: Optional[Decimal] = None
    DetalleProducto_Stock: Optional[int] = None

class DetalleProductoOut(DetalleProductoBase):
    DetalleProducto_ID: int
    model_config = {"from_attributes": True}


# ── OrdenTransporte ────────────────────────────────────────
class OrdenTransporteBase(BaseModel):
    Orden_FechaEmision: Optional[date] = None
    Orden_FechaEntrega: Optional[date] = None
    Orden_Cantidad: Optional[int] = None
    Orden_DetalleProducto_ID: int
    Orden_Transporte_ID: int

class OrdenTransporteCreate(OrdenTransporteBase): pass

class OrdenTransporteUpdate(BaseModel):
    Orden_FechaEmision: Optional[date] = None
    Orden_FechaEntrega: Optional[date] = None
    Orden_Cantidad: Optional[int] = None
    Orden_DetalleProducto_ID: Optional[int] = None
    Orden_Transporte_ID: Optional[int] = None

class OrdenTransporteOut(OrdenTransporteBase):
    Orden_ID: int
    model_config = {"from_attributes": True}


# ── CabeceraFactura ────────────────────────────────────────
class CabeceraFacturaBase(BaseModel):
    CabeceraFactura_NroFactura: str
    CabecerasFactura_Fecha: Optional[date] = None

class CabeceraFacturaCreate(CabeceraFacturaBase): pass

class CabeceraFacturaUpdate(BaseModel):
    CabeceraFactura_NroFactura: Optional[str] = None
    CabecerasFactura_Fecha: Optional[date] = None

class CabeceraFacturaOut(CabeceraFacturaBase):
    CabeceraFactura_ID: int
    model_config = {"from_attributes": True}


# ── MedioPago ──────────────────────────────────────────────
class MedioPagoBase(BaseModel):
    MedioPago_Nombre: str

class MedioPagoCreate(MedioPagoBase): pass

class MedioPagoUpdate(BaseModel):
    MedioPago_Nombre: Optional[str] = None

class MedioPagoOut(MedioPagoBase):
    MedioPago_ID: int
    model_config = {"from_attributes": True}


# ── Factura ────────────────────────────────────────────────
class FacturaBase(BaseModel):
    Factura_CabeceraFactura_ID: int
    Factura_MedioPago_ID: int
    Factura_Orden_ID: int

class FacturaCreate(FacturaBase): pass

class FacturaUpdate(BaseModel):
    Factura_CabeceraFactura_ID: Optional[int] = None
    Factura_MedioPago_ID: Optional[int] = None
    Factura_Orden_ID: Optional[int] = None

class FacturaOut(FacturaBase):
    Factura_ID: int
    model_config = {"from_attributes": True}
