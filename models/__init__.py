from sqlalchemy import Boolean, Column, Date, Numeric, ForeignKey, Integer, LargeBinary, SmallInteger, String
from sqlalchemy.orm import relationship
from core.database import Base


# ── Departamentos ──────────────────────────────────────────
class Departamento(Base):
    __tablename__ = "Departamentos"
    Dpto_ID = Column(Integer, primary_key=True, index=True)
    Dpto_Nombre = Column(String(18), nullable=False)

    provincias = relationship("Provincia", back_populates="departamento")


# ── Provincias ─────────────────────────────────────────────
class Provincia(Base):
    __tablename__ = "Provincias"
    Prov_ID = Column(SmallInteger, primary_key=True, index=True)
    Prov_Nombre = Column(String(27), nullable=False)
    Prov_Dpto_ID = Column(Integer, ForeignKey("Departamentos.Dpto_ID"), nullable=False)

    departamento = relationship("Departamento", back_populates="provincias")
    distritos = relationship("Distrito", back_populates="provincia")


# ── Distritos ──────────────────────────────────────────────
class Distrito(Base):
    __tablename__ = "Distritos"
    Distrito_ID = Column(SmallInteger, primary_key=True, index=True)
    Distrito_Nombre = Column(String(36), nullable=False)
    Distrito_Prov_ID = Column(SmallInteger, ForeignKey("Provincias.Prov_ID"), nullable=False)

    provincia = relationship("Provincia", back_populates="distritos")
    direcciones = relationship("Direccion", back_populates="distrito")
    flotas = relationship("Flota", back_populates="distrito")


# ── Direcciones ────────────────────────────────────────────
class Direccion(Base):
    __tablename__ = "Direcciones"
    Direccion_ID = Column(Integer, primary_key=True, index=True)
    Direccion_Nombre = Column(String(120), nullable=False)
    Direccion_Latitud = Column(Numeric(12, 9))
    Direccion_Altitud = Column(Numeric(12, 9))
    Direccion_Distrito_ID = Column(SmallInteger, ForeignKey("Distritos.Distrito_ID"), nullable=False)

    distrito = relationship("Distrito", back_populates="direcciones")
    consumidores = relationship("Consumidor", back_populates="direccion")
    puntos_venta = relationship("PuntoVenta", back_populates="direccion")
    centros_acopio = relationship("CentroAcopio", back_populates="direccion")


# ── Usuarios ───────────────────────────────────────────────
class Usuario(Base):
    __tablename__ = "Usuarios"
    Usuario_ID = Column(Integer, primary_key=True, index=True)
    Usuario_Nombres = Column(String(50), nullable=False)
    Usuario_Apellidos = Column(String(50), nullable=False)
    Usuario_FechaNacimiento = Column(Date)
    Usuario_DNI = Column(String(8), unique=True, nullable=False)
    Usuario_Rol = Column(String(1), nullable=False)
    Usuario_Password = Column(String(150), nullable=False)

    telefonos = relationship("Telefono", back_populates="usuario")
    conductor = relationship("Conductor", back_populates="usuario", uselist=False)
    inspector = relationship("Inspector", back_populates="usuario", uselist=False)
    consumidor = relationship("Consumidor", back_populates="usuario", uselist=False)


# ── Telefonos ──────────────────────────────────────────────
class Telefono(Base):
    __tablename__ = "Telefonos"
    Telefono_ID = Column(Integer, primary_key=True, index=True)
    Telefono_Nro = Column(String(9), nullable=False)
    Telefono_Prefijo = Column(String(5))
    Telefono_Usuario_ID = Column(Integer, ForeignKey("Usuarios.Usuario_ID"), nullable=False)

    usuario = relationship("Usuario", back_populates="telefonos")


# ── Conductores ────────────────────────────────────────────
class Conductor(Base):
    __tablename__ = "Conductores"
    Conductor_ID = Column(Integer, primary_key=True, index=True)
    Conductor_Licencia = Column(Boolean, default=False)
    Conductor_Antecedentes = Column(Boolean, default=False)
    Conductor_SeguroVehicular = Column(Boolean, default=False)
    Conductor_Usuario_ID = Column(Integer, ForeignKey("Usuarios.Usuario_ID"), nullable=False)

    usuario = relationship("Usuario", back_populates="conductor")
    transportes = relationship("Transporte", back_populates="conductor")


# ── Inspectores ────────────────────────────────────────────
class Inspector(Base):
    __tablename__ = "Inspectores"
    Inspector_ID = Column(SmallInteger, primary_key=True, index=True)
    Inspector_CV = Column(LargeBinary)
    Inspector_Usuario_ID = Column(Integer, ForeignKey("Usuarios.Usuario_ID"), nullable=False)

    usuario = relationship("Usuario", back_populates="inspector")
    reportes_calidad = relationship("ReporteCalidad", back_populates="inspector")


# ── Transportes ────────────────────────────────────────────
class Transporte(Base):
    __tablename__ = "Transportes"
    Transporte_ID = Column(Integer, primary_key=True, index=True)
    Transporte_NroPlaca = Column(String(8), nullable=False)
    Transporte_Conductor_ID = Column(Integer, ForeignKey("Conductores.Conductor_ID"), nullable=False)

    conductor = relationship("Conductor", back_populates="transportes")
    flotas = relationship("Flota", back_populates="transporte")
    ordenes = relationship("OrdenTransporte", back_populates="transporte")


# ── Roles de Empresas ──────────────────────────────────────
class RolEmpresa(Base):
    __tablename__ = "Roles de Empresas"
    EmpresaRol_ID = Column(Integer, primary_key=True, index=True)
    EmpresaRol_Tipo = Column(String(1), nullable=False)

    empresas = relationship("Empresa", back_populates="rol")


# ── Tipos de Canales de Atencion ───────────────────────────
class TipoCanal(Base):
    __tablename__ = "Tipos de Canales de Atencion"
    TipoCanal_ID = Column(Integer, primary_key=True, index=True)
    TipoCanal_Nombre = Column(String(1), nullable=False)

    canales = relationship("Canal", back_populates="tipo_canal")


# ── Empresas ───────────────────────────────────────────────
class Empresa(Base):
    __tablename__ = "Empresas"
    Empresa_ID = Column(SmallInteger, primary_key=True, index=True)
    Empresa_Nombre = Column(String(150), nullable=False)
    Empresa_RazonSocial = Column(String(150))
    Empresa_Rol_ID = Column(Integer, ForeignKey("Roles de Empresas.EmpresaRol_ID"), nullable=False)

    rol = relationship("RolEmpresa", back_populates="empresas")
    canales = relationship("Canal", back_populates="empresa")
    productos = relationship("Producto", back_populates="empresa")


# ── Canales ────────────────────────────────────────────────
class Canal(Base):
    __tablename__ = "Canales"
    Canal_ID = Column(Integer, primary_key=True, index=True)
    Canal_Enlace = Column(String(50), nullable=False)
    Canal_TipoCanal_ID = Column(Integer, ForeignKey("Tipos de Canales de Atencion.TipoCanal_ID"), nullable=False)
    Canal_Empresa_ID = Column(SmallInteger, ForeignKey("Empresas.Empresa_ID"), nullable=False)

    tipo_canal = relationship("TipoCanal", back_populates="canales")
    empresa = relationship("Empresa", back_populates="canales")


# ── Consumidores ───────────────────────────────────────────
class Consumidor(Base):
    __tablename__ = "Consumidores"
    Consumidor_ID = Column(Integer, primary_key=True, index=True)
    Consumidor_Direccion_ID = Column(Integer, ForeignKey("Direcciones.Direccion_ID"), nullable=False)
    Consumidor_Usuario_ID = Column(Integer, ForeignKey("Usuarios.Usuario_ID"), nullable=False)

    direccion = relationship("Direccion", back_populates="consumidores")
    usuario = relationship("Usuario", back_populates="consumidor")


# ── Flotas ─────────────────────────────────────────────────
class Flota(Base):
    __tablename__ = "Flotas"
    Flota_ID = Column(SmallInteger, primary_key=True, index=True)
    Flota_Distrito_ID = Column(SmallInteger, ForeignKey("Distritos.Distrito_ID"), nullable=False)
    Flota_Transporte_ID = Column(Integer, ForeignKey("Transportes.Transporte_ID"), nullable=False)

    distrito = relationship("Distrito", back_populates="flotas")
    transporte = relationship("Transporte", back_populates="flotas")
    puntos_venta = relationship("PuntoVenta", back_populates="flota")


# ── Puntos de Venta ────────────────────────────────────────
class PuntoVenta(Base):
    __tablename__ = "Puntos de Venta"
    PuntoVenta_ID = Column(Integer, primary_key=True, index=True)
    PuntoVenta_Nombre = Column(String(80), nullable=False)
    PuntoVenta_Direccion_ID = Column(Integer, ForeignKey("Direcciones.Direccion_ID"), nullable=False)
    PuntoVenta_Flota_ID = Column(SmallInteger, ForeignKey("Flotas.Flota_ID"), nullable=False)

    direccion = relationship("Direccion", back_populates="puntos_venta")
    flota = relationship("Flota", back_populates="puntos_venta")


# ── Centros de Acopio ──────────────────────────────────────
class CentroAcopio(Base):
    __tablename__ = "Centros de Acopio"
    CentroAcopio_ID = Column(Integer, primary_key=True, index=True)
    CentroAcopio_Nombre = Column(String(150), nullable=False)
    CentroAcopio_CapacidadTotal = Column(Integer)
    CentroAcopio_Direccion_ID = Column(Integer, ForeignKey("Direcciones.Direccion_ID"), nullable=False)

    direccion = relationship("Direccion", back_populates="centros_acopio")
    productos = relationship("Producto", back_populates="centro_acopio")


# ── Inspectores → Reportes de Calidad → Productos (circular) ─
class ReporteCalidad(Base):
    __tablename__ = "Reportes de Calidad"
    ReporteCalidad_ID = Column(Integer, primary_key=True, index=True)
    ReporteCalidad_Fecha = Column(Date)
    ReporteCalidad_Documento = Column(LargeBinary)
    ReporteCalidad_Inspector_ID = Column(SmallInteger, ForeignKey("Inspectores.Inspector_ID"), nullable=False)

    inspector = relationship("Inspector", back_populates="reportes_calidad")
    producto = relationship("Producto", back_populates="reporte_calidad", uselist=False)


# ── Productos ──────────────────────────────────────────────
class Producto(Base):
    __tablename__ = "Productos"
    Producto_ID = Column(Integer, primary_key=True, index=True)
    Producto_Nombre = Column(String(150), nullable=False)
    Producto_Codigo = Column(String(50), unique=True, nullable=False)
    Producto_Empresa_ID = Column(SmallInteger, ForeignKey("Empresas.Empresa_ID"), nullable=False)
    Producto_ReporteCalidad_ID = Column(Integer, ForeignKey("Reportes de Calidad.ReporteCalidad_ID"))
    Producto_CentroAcopio_ID = Column(Integer, ForeignKey("Centros de Acopio.CentroAcopio_ID"), nullable=False)

    empresa = relationship("Empresa", back_populates="productos")
    reporte_calidad = relationship("ReporteCalidad", back_populates="producto")
    centro_acopio = relationship("CentroAcopio", back_populates="productos")
    detalles = relationship("DetalleProducto", back_populates="producto")


# ── Detalles de Productos ──────────────────────────────────
class DetalleProducto(Base):
    __tablename__ = "Detalles de Productos"
    DetalleProducto_ID = Column(Integer, primary_key=True, index=True)
    DetalleProducto_FechaVencimiento = Column(Date)
    DetalleProducto_PrecioUnitario = Column(Numeric(5, 2))
    DetalleProducto_Stock = Column(SmallInteger)
    DetalleProducto_Producto_ID = Column(Integer, ForeignKey("Productos.Producto_ID"), nullable=False)

    producto = relationship("Producto", back_populates="detalles")
    ordenes = relationship("OrdenTransporte", back_populates="detalle_producto")


# ── Ordenes de Transporte ──────────────────────────────────
class OrdenTransporte(Base):
    __tablename__ = "Ordenes de Transporte"
    Orden_ID = Column(Integer, primary_key=True, index=True)
    Orden_FechaEmision = Column(Date)
    Orden_FechaEntrega = Column(Date)
    Orden_Cantidad = Column(SmallInteger)
    Orden_DetalleProducto_ID = Column(Integer, ForeignKey("Detalles de Productos.DetalleProducto_ID"), nullable=False)
    Orden_Transporte_ID = Column(Integer, ForeignKey("Transportes.Transporte_ID"), nullable=False)

    detalle_producto = relationship("DetalleProducto", back_populates="ordenes")
    transporte = relationship("Transporte", back_populates="ordenes")
    factura = relationship("Factura", back_populates="orden", uselist=False)


# ── Cabeceras de Facturas ──────────────────────────────────
class CabeceraFactura(Base):
    __tablename__ = "Cabeceras de Facturas"
    CabeceraFactura_ID = Column(Integer, primary_key=True, index=True)
    CabeceraFactura_NroFactura = Column(String(50), unique=True, nullable=False)
    CabecerasFactura_Fecha = Column(Date)

    factura = relationship("Factura", back_populates="cabecera", uselist=False)


# ── Medios de Pago ─────────────────────────────────────────
class MedioPago(Base):
    __tablename__ = "Medios de Pago"
    MedioPago_ID = Column(Integer, primary_key=True, index=True)
    MedioPago_Nombre = Column(String(1), nullable=False)

    facturas = relationship("Factura", back_populates="medio_pago")


# ── Facturas ───────────────────────────────────────────────
class Factura(Base):
    __tablename__ = "Facturas"
    Factura_ID = Column(Integer, primary_key=True, index=True)
    Factura_CabeceraFactura_ID = Column(Integer, ForeignKey("Cabeceras de Facturas.CabeceraFactura_ID"), nullable=False)
    Factura_MedioPago_ID = Column(Integer, ForeignKey("Medios de Pago.MedioPago_ID"), nullable=False)
    Factura_Orden_ID = Column(Integer, ForeignKey("Ordenes de Transporte.Orden_ID"), nullable=False)

    cabecera = relationship("CabeceraFactura", back_populates="factura")
    medio_pago = relationship("MedioPago", back_populates="facturas")
    orden = relationship("OrdenTransporte", back_populates="factura")
